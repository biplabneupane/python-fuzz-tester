import json
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "crashes.json")

# Ensure the logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_info(message):
    """Logs general information (not crashes)."""
    print(f"ℹ️ INFO: {message}")

def log_crash(input_str, error_message):
    """Logs crashes in a JSON file."""
    print(f"⚠️ Crash detected! Logging input: {repr(input_str)}")

    crash_entry = {
        "input": input_str,
        "error": error_message
    }

    try:
        # Append to JSON file safely
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                json.dump([crash_entry], f, indent=4)
        else:
            with open(LOG_FILE, "r+") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        data.append(crash_entry)
                    else:
                        data = [crash_entry]
                except json.JSONDecodeError:
                    data = [crash_entry]

                f.seek(0)
                json.dump(data, f, indent=4)
    except Exception as e:
        print(f"❌ Error while logging crash: {e}")
