import streamlit as st
from llm import History, llm_chat

from video_review import extract_audio_from_video, transcribe_audio

# Set up Streamlit app layout
st.title("Recipe Extraction from Video")
st.write("Upload a video to extract and transcribe its recipe")

# File uploader widget for video upload
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov"])

if uploaded_file is not None:
    # Define paths for the uploaded video and output files
    video_path = f"data/{uploaded_file.name}"
    if "mp4" in video_path:
        audio_path = video_path.replace(".mp4", ".mp3")
        json_path = video_path.replace(".mp4", ".json")
    else:
        audio_path = video_path.replace(".mov", ".mp3")
        json_path = video_path.replace(".mov", ".json")

    # Save the uploaded video file
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded video file: {uploaded_file.name}")

    # Step 1: Extract audio from the video
    extracted_audio = extract_audio_from_video(video_path, audio_path)
    st.success(f"Audio extracted: {audio_path}")

    # Step 2: Transcribe the audio
    transcription = transcribe_audio(extracted_audio)
    st.write("**Transcription:**")
    st.write(transcription)

    history = History()
    history.system("You are a recipe extractor from video transcript:")
    history.user("Video Transcript: " + transcription)
    answer = llm_chat(history)
    st.write("**Recipe**")
    st.write(answer)

else:
    st.write("Please upload a video file to start.")
