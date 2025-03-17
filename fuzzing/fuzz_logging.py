import json
import os
from datetime import datetime

LOG_DIR = "logs"
CRASH_LOG = os.path.join(LOG_DIR, "crashes.json")

def log_info(message):
    """Logs general fuzzing information."""
    print(message)

def log_crash(input_str, error_message):
    """Logs crashes in a structured format (JSON)."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    crash_data = {
        "timestamp": datetime.now().isoformat(),
        "input": input_str,
        "error": error_message
    }

    try:
        if os.path.exists(CRASH_LOG):
            with open(CRASH_LOG, "r", encoding="utf-8") as f:
                crashes = json.load(f)
        else:
            crashes = []

        crashes.append(crash_data)

        with open(CRASH_LOG, "w", encoding="utf-8") as f:
            json.dump(crashes, f, indent=4)
        
        print(f"⚠️ Crash logged: {error_message}")

    except Exception as e:
        print(f"❌ Failed to log crash: {e}")
