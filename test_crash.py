import json
import os

LOGS_DIR = "logs"
CRASH_LOG_FILE = os.path.join(LOGS_DIR, "crashes.json")

def log_crash(input_data, error_message):
    """Logs crashes to a JSON file."""
    print(f"🚨 Logging crash: {input_data} -> {error_message}")  # Debugging
    os.makedirs(LOGS_DIR, exist_ok=True)  # Ensure logs directory exists

    crashes = []
    if os.path.exists(CRASH_LOG_FILE):
        try:
            with open(CRASH_LOG_FILE, "r", encoding="utf-8") as f:
                crashes = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Warning: crashes.json is corrupted. Creating a new file.")

    crashes.append({"input": input_data, "error": error_message})

    with open(CRASH_LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(crashes, f, indent=4)

    print(f"✅ Crash logged successfully in {CRASH_LOG_FILE}")

# Run test
log_crash("test_input", "Simulated crash error")
