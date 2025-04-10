from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import config

def get_slack_client():
    return WebClient(token=config.SLACK_TOKEN)

def send_message(channel, text):
    client = get_slack_client()
    try:
        response = client.chat_postMessage(channel=channel, text=text)
        return True, "Message sent successfully!"
    except SlackApiError as e:
        return False, f"Error: {e.response['error']}"

def send_image(channel, image_url, text=""):
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
    channel_name = channel_name.startswith("#") and channel_name[1:] or channel_name
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
