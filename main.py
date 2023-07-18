# Install dependencies

# Windows

#Installing pytorch


#Installing whisper

#streamlit

import streamlit as st
import whisper

st.title("Whisper App")

audio_file = st.file_uploader("Upload audio", type =['wav', "mp3", "m4a"])
video_file = st.file_uploader("Upload video", type =['mp4', "webm", "mov"])
model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if st.sidebar.button("Transcribe Video"):
    if video_file is not None:
        st.sidebar.success("Transcribing Video")    
        transcription = model.transcribe(video_file.name)
        st.sidebar.success("Transcription Complete")
        st.subheader(transcription["text"])

    else:
        st.sidebar.error("Please upload a video file", icon="🚨")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")    
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.subheader(transcription["text"])

    else:
        st.sidebar.error("Please upload an audio file", icon="🚨")  


st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)         



st.sidebar.header("Play Original Video")
st.sidebar.video(video_file)