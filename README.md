# Speech-to-Text Web Application

This project is a web-based speech-to-text application that converts audio input into text using OpenAI’s Whisper model. It is built using Flask for the backend and provides a simple interface for uploading audio files and receiving transcriptions.

## Features

* Upload audio files (WAV, MP3, M4A, etc.)
* Convert speech to text using Whisper
* Simple web interface
* Supports multiple languages (depending on model)
* Can be extended with keyword extraction

## Tech Stack

* Python
* Flask
* Whisper (OpenAI)
* PyTorch
* FFmpeg
* HTML/CSS

## How It Works

1. The user uploads an audio file through the web interface.
2. The Flask server receives and temporarily stores the file.
3. The audio is processed using FFmpeg to ensure it is in the correct format.
4. The Whisper model converts the processed audio into text.
5. The transcribed text is returned and displayed on the webpage.

## Project Structure

speech-to-text/
│
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
├── uploads/
├── requirements.txt
└── README.md


## Limitations

* Accuracy may drop with noisy or unclear audio
* Processing time depends on system performance
* Not suitable for real-time transcription
* Large audio files can take longer to process

## Future Improvements

* Real-time microphone input
* Speaker identification
* Improved UI/UX
* Text summarization and keyword extraction
* Cloud deployment

## Use Cases

* Lecture transcription
* Meeting notes
* Content creation
* Accessibility support

## License

This project is for educational purposes.
