import logging

def setup_logging(log_file, level=logging.INFO):
    logger = logging.getLogger("media_system")
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger

# Usage example:
# logger = setup_logging(Config.LOG_FILE)
# logger.info("File uploaded: %s", file_id)
