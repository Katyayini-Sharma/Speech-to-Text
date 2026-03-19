import whisper

model = None  # lazy loading


def transcribe_audio(file_path):
    global model

    if model is None:
        model = whisper.load_model("small")

    result = model.transcribe(
        file_path,
        fp16=False
    )

    print("RAW TEXT:", result["text"])

    return {
        "text": result["text"],
        "language": result["language"],
        "segments": result["segments"]
    }