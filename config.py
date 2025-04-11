import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SLACK_TOKEN = os.getenv('SLACK_BOT_TOKEN')
DEFAULT_CHANNEL = os.getenv('SLACK_DEFAULT_CHANNEL')
