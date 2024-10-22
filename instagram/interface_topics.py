import streamlit as st

from files import json_read_file
from transcripts import generate_topic


# Streamlit app
def main():
    st.title("Transcript Generator")

    # Load transcripts from JSON
    data = json_read_file("data/reset_energia.json")
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