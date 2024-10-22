from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_core.documents import Document

from files import json_read_file
from llm import History
from streaming_logo import streaming_logo_interface

# Global flag to track if the thread has started
transcript_thread_started = False


if __name__ == "__main__":
    company_name = "Reset Energia"
    emoji = "🪞"
    company_id = "reset_energia"
    # Main program logic (call this function when you want to start the thread)
    try:
        data = json_read_file(f"data/{company_id}.json")
        if data is None:
            st.error("Error: Transcripts file not found.")
            raise Exception("error")
        pages = [Document(page_content=post["transcript"]) for post in data["posts"]]
        print(len(pages))
        history = History()
        #print("rerun")
        #history.assistant("Hi, I’m Julia. What would you like to know?")
        #print(len(history.logs))
        #streaming_logo_interface(company_name, emoji, history, pages=pages)
    except KeyboardInterrupt:
        print("Program interrupted.")

