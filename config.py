import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SLACK_APP_ID = os.getenv('SLACK_APP_ID')
SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
SLACK_VERIFICATION_TOKEN = os.getenv('SLACK_VERIFICATION_TOKEN')
SLACK_TOKEN = os.getenv('SLACK_BOT_TOKEN')  # Changed from APP_TOKEN to BOT_TOKEN
DEFAULT_CHANNEL = os.getenv('SLACK_DEFAULT_CHANNEL')
