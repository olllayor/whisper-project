#Streamlit Whisper App

## Overview
The Whisper App is designed to transcribe audio and video files using the Whisper model. Users can upload audio or video files in various formats and transcribe their contents using the loaded model.

## Installation
### Dependencies
This app requires the following dependencies to be installed:
- Python packages:
  - `streamlit`
  - `whisper`
- Additionally, for Windows, ensure PyTorch is installed.

### Steps to Install Dependencies
1. Install Python packages:
pip install streamlit whisper


2. Install PyTorch for Windows (if not already installed):
- Follow the instructions on the [PyTorch website](https://pytorch.org/) to install the appropriate version for your system.

## Usage
1. Run the application:
streamlit run app.py

2. Once the app is running, you'll see the Whisper App interface in your browser.
3. Upload an audio or video file:
- For audio, you can upload files in formats like WAV, MP3, or M4A.
- For video, supported formats include MP4, WebM, or MOV.
4. Load the Whisper model by clicking on the appropriate button.
5. To transcribe the uploaded audio or video file:
- Click the "Transcribe Audio" or "Transcribe Video" button respectively.
- If no file is uploaded, an error message will prompt you to upload a file.
6. The transcribed text will appear in the app interface once the transcription process is complete.

## Interface
- **File Upload**: Users can upload audio and video files.
- **Transcription Buttons**: Click to transcribe the uploaded files.
- **Sidebar**:
- Displays transcriptions and allows playback of the original audio and video files.
