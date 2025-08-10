import os

class Config:
    UPLOAD_DIR = os.environ.get('UPLOAD_DIR', './uploads/')
    DATA_FILE = os.environ.get('DATA_FILE', './media_db.pkl')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 2 * 1024 * 1024 * 1024))  # 2GB default
    NOTIFY_EMAIL = os.environ.get('NOTIFY_EMAIL', 'admin@example.com')
    METADATA_DB_URI = os.environ.get('METADATA_DB_URI', 'sqlite:///metadata.db')
    VIRUS_SCAN_ENABLED = bool(int(os.environ.get('VIRUS_SCAN_ENABLED', 0)))
    LOG_FILE = os.environ.get('LOG_FILE', './app.log')
