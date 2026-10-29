import logging
import os
from logging.handlers import RotatingFileHandler
import from_root
from datetime import datetime


# Comstants for Log Configuration:
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024
BACKUP_COUNT = 3

# Construct Log File Path:
log_dir_path = os.path.join(from_root.from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.

    """

    # Create a custom logger
    logger = logging.getlogger()
    logger.setLevel(logging.DEBUG)

    # Define Formatter:
    formatter = logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s - %(message)s")

    # File Handler with rotation:
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupcount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console Handler:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handler to the logger:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Configure the logger:
configure_logger    