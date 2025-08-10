from infrastructure.config import Config
from infrastructure.logging import setup_logging

logger = setup_logging(Config.LOG_FILE)

if __name__ == "__main__":
    from adapters.in_rest.api import app
    app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH
    app.secret_key = Config.SECRET_KEY
    logger.info("App starting with upload directory: %s", Config.UPLOAD_DIR)
    app.run(debug=True)
