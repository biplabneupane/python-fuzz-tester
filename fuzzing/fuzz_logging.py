import json
import os
import csv
from datetime import datetime, timezone

LOG_DIR = "logs"
CRASH_LOG = os.path.join(LOG_DIR, "crashes.json")
FUZZ_DATA_LOG = os.path.join(LOG_DIR, "fuzz_data.csv")

os.makedirs(LOG_DIR, exist_ok=True)

def log_info(message):
    print(message)

def log_crash(input_data, error_message):
    log_info(f"⚠️ Crash detected: {repr(input_data)} - Error: {error_message}")

    crash_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input": input_data,
        "error": error_message,
        "input_length": len(input_data),
    }

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

    log_fuzz_data(input_data, crashed=1, error=error_message)


def log_fuzz_data(input_data, crashed=0, error="None"):
    file_exists = os.path.isfile(FUZZ_DATA_LOG)

    with open(FUZZ_DATA_LOG, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "input_text", "input_length", "crashed", "error"])  
        writer.writerow([ datetime.now(timezone.utc).isoformat(), input_data, len(input_data), crashed, error])
