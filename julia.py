from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_core.documents import Document

from files import json_read_file
from llm import History
from streaming_logo import streaming_logo_interface

# Global flag to track if the thread has started


def main():
    st.set_page_config(
        page_title=f"Reset Energia",
        page_icon="🔋",
        layout="wide",
    )

    st.title("Reset Energia")

    # Load transcripts from JSON
    data = json_read_file("data/reset_energia.json")
    if data is None:
        st.error("Error: Transcripts file not found.")
        return

    history = History()
    history.system("You are a transcript analyzer, to come up with future transcripts that follow a similar pattern:")
    history.system(
        """Foreword: First of all the band I'm working for as a social media strategist and content will deal with selling green light energy (service not active yet). as of now the page deals with telling through reels with fresh and young tov, all those possible problems, life in general that we all have to face alone/ with family/ as a couple or with roommates. in the reels we explain how to save money, how to make greener and eco decisions and how to solve messes that you don't know how to do e.g. how do I wash clothes? What do I put in the dishwasher? What are the symbols I find on clothes to wash them?""")
    history.system("""Objectives: To create a community of people who are not only on the ig page to learn but also to have their say, give input on how they make a living and manage household chores. Our reels want to not only explain but also for them to be a source of debate among users and inspiration to each other.

    The rewards we will use both in stories and for reels/posts etc. 
    They are: self (content that provides useful information that can enrich users' personal experience. ), relatability(content that makes us think “omg he's talking about me.”) and social (content that creates appreciation for users by users themselves). 
    """)

    for post in data["posts"]:
        history.system("Transcript: " + post["transcript"])
    history.assistant("Hi, my name is Julia!")
    # Button to trigger transcript generation
    streaming_logo_interface("Reset Energia", history)


if __name__ == "__main__":
   main()
