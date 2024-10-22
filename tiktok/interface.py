import os
from typing import List

import rootpath
import streamlit as st

from files import json_read_file
from llm import History, llm_chat


# Function to generate a transcript based on a list of transcripts and a new topic
def generate_topic(transcripts: List):
    history = History()
    history.system("You are a transcript analyzer, to come up with future transcripts that follow a similar pattern:")
    for transcript in transcripts:
        history.system("Transcript: " + transcript)
    history.system("What type of tone and personality is represented in the transcripts?")
    personality = llm_chat(history)
    history.assistant(personality)

    history.system("Generate a topic for future videos, using pumpkins for dinner recipes suggest the title of the topic:")
    topic = llm_chat(history, temperature=1.0)
    history.assistant(topic)

    history.system("Generate a new transcript in line with the tone and personality previously "
                   "described for the suggested topic: ")
    transcript = llm_chat(history)
    history.assistant(transcript)

    return topic, transcript


# Streamlit app
def main():
    st.title("Transcript Generator")

    # Load transcripts from JSON
    file_path = os.path.join(rootpath.detect(), "tiktok", "data", "lisaoudijn.json")
    data = json_read_file(file_path)
    if data is None:
        st.error("Error: Transcripts file not found.")
        return
    transcripts = [post["transcript"] for post in data["posts"]]

    # Button to trigger transcript generation
    if st.button("Generate Topic idea and Transcript for next video"):
        with st.spinner("Generating topic and transcript..."):
            topic, transcript = generate_topic(transcripts)
            st.success("Transcript generated!")
            st.header(topic)
            st.write(transcript)


if __name__ == "__main__":
    main()
