from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import config

def get_slack_client():
    """Creates a Slack client using the token from the config."""
    return WebClient(token=config.SLACK_TOKEN)

def send_message(channel, text):
    """Sends a message to a Slack channel."""
    client = get_slack_client()

    try:
        # ref: https://tools.slack.dev/python-slack-sdk/web/#sending-a-message
        response = client.chat_postMessage(channel=channel, text=text)
        return True, "Message sent successfully!"
    except SlackApiError as e:
        return False, f"Error: {e.response['error']}"

def send_image(channel, image_url, text=""):
    """Sends an image to a Slack channel."""
    client = get_slack_client()

    try:
        response = client.chat_postMessage(
            channel=channel,
            blocks=[
                {
                    "type": "image",
                    "title": {"type": "plain_text", "text": text},
                    "image_url": image_url,
                    "alt_text": text
                }
            ]
        )
        return True, "Image sent successfully!"
    except SlackApiError as e:
        return False, f"Error: {e.response['error']}"

def get_channel_id(channel_name):

    client = get_slack_client()
    channel_name = channel_name[1:] if channel_name.startswith("#") else channel_name
    try:
        result = client.conversations_list()

        if result and result.get("channels"):
            for channel in result["channels"]:
                if channel["name"] == channel_name:
                    return channel["id"]
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def send_file(channel, file_path, title=""):
    client = get_slack_client()

    # for files we need to get the channel id instead of
    # just using the channel name. See:
    # https://stackoverflow.com/a/77790657
    channel_id = get_channel_id(channel)

    try:
        response = client.files_upload_v2(
            channel=channel_id,
            file=file_path,
            title=title,
        )
        return True, "File sent successfully!"
    except SlackApiError as e:
        print("Error:", e.response)
        return False, f"Error: {e.response['error']}"
