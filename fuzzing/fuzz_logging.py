import logging
import os

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Setup logging with file output
LOG_FILE = os.path.join(LOG_DIR, "fuzz.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Print logs to console too
    ]
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def log_crash(input_data, error_message):
    """Logs crashes separately for better debugging."""
    crash_file = os.path.join(LOG_DIR, "crashes.log")
    with open(crash_file, "a") as f:
        f.write(f"Crash found! Input: {repr(input_data)} | Error: {error_message}\n")
    logging.error(f"❌ Crash logged: {repr(input_data)} | {error_message}")
