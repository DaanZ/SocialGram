from files import json_read_file, json_write_file
from video_review import extract_audio_from_video, transcribe_audio

video_path = "data/lisaoudijn.json"
data = json_read_file(video_path)

for row in data["posts"]:
    print(row)
    if "audio" in row:
        continue

    # Extract audio from the video
    audio_path = row["video"].replace("mp4", "mp3")
    extracted_audio = extract_audio_from_video(row["video"], audio_path)
    row["audio"] = audio_path
    json_write_file(video_path, data)

    if "transcript" in row:
        continue

    # Transcribe the audio
    transcription = transcribe_audio(extracted_audio)
    row["transcript"] = transcription
    json_write_file(video_path, data)

print("done")