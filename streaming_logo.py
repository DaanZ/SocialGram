import base64
import os

import rootpath
import streamlit as st
from langchain_openai import ChatOpenAI

from llm import History, process_stream, llm_stream

chat = ChatOpenAI(model="gpt-o1")


def streaming_logo_interface(company_name: str, history: History, optional: str = "", prompt=None, pages=None, background: str = "background.png"):

    # Function to load image and convert to Base64
    def load_image(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string

    # Load the Gaia image (for background)
    background_image = load_image(os.path.join(rootpath.detect(),"images", background))

    # Custom CSS to set the background image to the right and 50% of the width
    st.markdown(f"""
        <style>
        /* Set the background image on the right side taking up 50% width */
        .stApp {{
            background-image: url("data:image/png;base64,{background_image}");
            background-size: 100% auto; /* 50% of the width, auto for height */
            background-position: center center; /* Centered vertically, right-aligned */
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns([7, 3])
    with col1:
        # Initialize history if not already in session state
        if "history" not in st.session_state.keys():
            st.session_state.history = history
            if prompt is None:
                st.session_state.history.system(
                    f"""You are a very kindly and friendly marketing assistant for {company_name}. 
                You are currently having a conversation with a marketing person. Answer the questions in a kind and friendly 
                way, being the expert for {company_name} to answer any questions about marketing.""")
            else:
                st.session_state.history.system(prompt)

            if optional:
                st.session_state.history.system(optional)
                with st.chat_message("system"):
                    st.markdown(optional)

        # Display all previous messages
        for message in st.session_state.history.logs:
            if message["role"] == "system":
                continue
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    user_prompt = st.chat_input()  # Input box for the user

    with col1:
        if user_prompt is not None:
            st.session_state.history.user(user_prompt)
            with st.chat_message("user"):
                st.markdown(user_prompt)

            # Placeholder for the assistant's reply
            assistant_message_placeholder = st.chat_message("assistant")
            assistant_text = assistant_message_placeholder.empty()

            # Stream response
            with st.spinner("Loading..."):
                response_stream = llm_stream(st.session_state.history)
                answers = process_stream(response_stream)
                chunk = ""
                for chunk in answers:
                    assistant_text.markdown(chunk)  # Update progressively
                st.session_state.history.assistant(chunk)  # Save final message in history
