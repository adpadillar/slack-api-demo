import streamlit as st
import config
from slack_utils import send_message, send_image, send_file

st.title("Slack Message Sender")

# Channel input
channel = st.text_input("Slack Channel", value=config.DEFAULT_CHANNEL)

# Message type selector
message_type = st.selectbox(
    "Select message type",
    ["Text Message", "Image Message", "File Upload"]
)

if message_type == "Text Message":
    message = st.text_area("Enter your message")
    if st.button("Send Text Message"):
        if message:
            success, response = send_message(channel, message)
            st.write(response)
        else:
            st.error("Please enter a message")

elif message_type == "Image Message":
    image_url = st.text_input("Enter image URL")
    image_caption = st.text_input("Image caption (optional)")
    if st.button("Send Image"):
        if image_url:
            success, response = send_image(channel, image_url, image_caption)
            st.write(response)
        else:
            st.error("Please enter an image URL")

else:  # File Upload
    uploaded_file = st.file_uploader("Choose a file")
    file_title = st.text_input("File title (optional)")
    if st.button("Send File"):
        if uploaded_file:
            # Save uploaded file temporarily
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
            success, response = send_file(channel, uploaded_file.name, file_title)
            # Clean up
            import os
            os.remove(uploaded_file.name)
            st.write(response)
        else:
            st.error("Please upload a file")
