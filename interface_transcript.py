import streamlit as st
from dotenv import load_dotenv

from files import json_read_file
from transcripts import generate_transcript

load_dotenv()


# Streamlit app
def main():
    st.title("Transcript Generator")

    # Textbox for inputting new topic
    topic = st.text_input("Enter the topic for the new transcript:")

    # Load transcripts from JSON
    data = json_read_file("data/reset_energia.json")
    if data is None:
        st.error("Error: Transcripts file not found.")
        return
    transcripts = [post["transcript"] for post in data["posts"]]

    # Button to trigger transcript generation
    if st.button("Generate Transcript"):
        if topic:
            with st.spinner("Generating transcript..."):
                transcript = generate_transcript(transcripts, topic)
                st.success("Transcript generated!")
                st.write(transcript)
        else:
            st.error("Please enter a topic before generating the transcript.")


if __name__ == "__main__":
    main()
