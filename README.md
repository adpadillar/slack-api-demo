# Streamlit Slack Messenger

A simple Streamlit web application that allows you to send messages, images, and files to Slack channels.

## Features

- Send text messages to Slack channels
- Share images via URL
- Upload and send files
- User-friendly web interface
- Configurable default channel

## Prerequisites

- Python 3.x
- Slack workspace with bot token
- Required Python packages (installed via requirements.txt)

## Installation

1. Clone the repository
2. Create a `.env` file in the project root with the following variables:

```
SLACK_APP_ID=your_app_id
SLACK_CLIENT_ID=your_client_id
SLACK_CLIENT_SECRET=your_client_secret
SLACK_SIGNING_SECRET=your_signing_secret
SLACK_VERIFICATION_TOKEN=your_verification_token
SLACK_BOT_TOKEN=your_bot_token
SLACK_DEFAULT_CHANNEL=#your-default-channel
```

3. Run the setup script to create a virtual environment and install dependencies:

```bash
./setup.sh
```

## Usage

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Start the Streamlit app:

```bash
streamlit run app.py
```

3. Open your browser and navigate to the provided local URL (usually http://localhost:8501)

## Features Description

- **Text Messages**: Send plain text messages to any Slack channel
- **Image Messages**: Share images by providing a URL and optional caption
- **File Upload**: Upload and share files directly to Slack channels

## Project Structure

- `app.py`: Main Streamlit application
- `config.py`: Configuration and environment variables management
- `slack_utils.py`: Slack API utility functions
- `requirements.txt`: Python dependencies
- `setup.sh`: Installation script
- `.env`: Environment variables (not tracked in git)

## Dependencies

- streamlit
- slack-sdk
- python-dotenv
- black (for code formatting)
- pylint (for code linting)

## Notes

- Make sure to have appropriate Slack bot permissions for sending messages, files, and accessing channels
- The app uses Slack's Bot Token for authentication
- Channel names can be provided with or without the '#' prefix
