import json
import os
import csv

LOG_DIR = "logs"
CRASH_LOG = os.path.join(LOG_DIR, "crashes.json")
FUZZ_DATA_LOG = os.path.join(LOG_DIR, "fuzz_data.csv")

# Ensure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_info(message):
    """Logs general fuzzing info."""
    print(message)

def log_crash(input_data, error_message):
    """Logs a crash input into a JSON file."""
    log_info(f"⚠️ Crash detected: {repr(input_data)} - Error: {error_message}")

    crash_entry = {"input": input_data, "error": error_message}

    # Append crash log to JSON
    crashes = []
    if os.path.exists(CRASH_LOG):
        with open(CRASH_LOG, "r") as f:
            try:
                crashes = json.load(f)
            except json.JSONDecodeError:
                pass

    crashes.append(crash_entry)
    
    with open(CRASH_LOG, "w") as f:
        json.dump(crashes, f, indent=4)

    # Log to fuzzing dataset
    log_fuzz_data(input_data, crashed=1)


def log_fuzz_data(input_data, crashed=0):
    """Logs all fuzzing inputs into CSV for ML training."""
    file_exists = os.path.isfile(FUZZ_DATA_LOG)

    with open(FUZZ_DATA_LOG, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["input_text", "crashed"])  # Add header if file is new
        writer.writerow([input_data, crashed])

