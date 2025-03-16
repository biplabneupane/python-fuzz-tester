import json
import os
import datetime

# Ensure the logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "fuzz_log.txt")
CRASH_FILE = os.path.join(LOG_DIR, "crashes.json")


def log_info(message):
    """Logs general information messages."""
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[INFO] {timestamp} - {message}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(log_entry)
    
    print(log_entry.strip())  # Also print to console


def log_crash(input_data, error_message):
    """Logs crash data with input and error details."""
    timestamp = datetime.datetime.now().isoformat()
    crash_data = {
        "timestamp": timestamp,
        "input": input_data,
        "error": error_message,
    }

    # Append to crashes.json
    crashes = []
    if os.path.exists(CRASH_FILE):
        with open(CRASH_FILE, "r", encoding="utf-8") as f:
            try:
                crashes = json.load(f)
            except json.JSONDecodeError:
                crashes = []  # Reset if file is corrupted
    
    crashes.append(crash_data)

    with open(CRASH_FILE, "w", encoding="utf-8") as f:
        json.dump(crashes, f, indent=4)

    # Also log crash in fuzz_log.txt
    log_entry = f"[CRASH] {timestamp} - Input: {repr(input_data)} - Error: {error_message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(log_entry)

    print(f"💥 Crash logged: {input_data} -> {error_message}")
