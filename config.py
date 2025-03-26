import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your-secret-key-here"
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    TRANSCRIPTION_FOLDER = os.path.join(os.getcwd(), "transcriptions")
    ALLOWED_EXTENSIONS = {
        "wav",
        "mp3",
        "ogg",
        "m4a",
        "flac",
        "mp4",
        "mpeg",
        "mpga",
        "webm",
    }
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
