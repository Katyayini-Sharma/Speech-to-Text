from flask import Flask, render_template, request, send_file
import os
import io
from transcribe import transcribe_audio
from record import record_audio

# PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

UPLOAD_FOLDER = "audio"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def get_full_language_name(code):
    languages = {
        "en": "English",
        "hi": "Hindi",
        "fr": "French",
        "es": "Spanish",
        "de": "German"
    }
    return languages.get(code, code.upper())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["audio"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    result = transcribe_audio(filepath)

    language = get_full_language_name(result["language"])
    return render_template("result.html", result=result, language=language)


@app.route("/record", methods=["POST"])
def record():
    filepath = record_audio()

    result = transcribe_audio(filepath)

    language = get_full_language_name(result["language"])
    return render_template("result.html", result=result, language=language)


# TXT download
@app.route("/download", methods=["POST"])
def download():
    text = request.form["text"]
    timestamps = request.form["timestamps"]

    content = f"Transcription:\n{text}\n\nTimestamps:\n{timestamps}"

    file = io.BytesIO()
    file.write(content.encode("utf-8"))
    file.seek(0)

    return send_file(
        file,
        as_attachment=True,
        download_name="transcription.txt",
        mimetype="text/plain"
    )


# PDF download
@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    text = request.form["text"]
    timestamps = request.form["timestamps"]

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("<b>Transcription</b><br/><br/>" + text, styles["Normal"]))
    content.append(Paragraph("<br/><b>Timestamps</b><br/><br/>" + timestamps, styles["Normal"]))

    doc.build(content)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="transcription.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    import os

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)