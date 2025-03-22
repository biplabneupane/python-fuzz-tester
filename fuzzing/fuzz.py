import csv
from datetime import datetime

def log_fuzz_data(input_data, crashed, error_message):
    timestamp = datetime.utcnow().isoformat()
    length = len(str(input_data)) if input_data is not None else 0

    with open('logs/fuzz_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, input_data, length, int(crashed), error_message])

def generate_test_inputs():
    return [
        "Hello, world!",
        "12345",
        "test@example.com",
        "",
        " " * 1000,
        "特殊字符",  # Special Unicode characters
        "<script>alert('XSS')</script>",
        "' OR '1'='1",  # SQL Injection
        "../../etc/passwd",  # Path traversal
        None,
        "a" * 1000000,  # Very long string
        "SELECT * FROM users WHERE id = 1",  # SQL Query
        "DROP TABLE users;",  # SQL Drop Command
        "{\"key\": \"value\"}",  # JSON String
        "2025-03-21T05:25:50",  # Date-Time String
    ]

def fuzz_target(input_data):
    try:
        # Simulate target function (replace with actual target)
        if input_data is None or not isinstance(input_data, str):
            raise ValueError("Input must be a string")
        if "../../" in input_data:
            raise FileNotFoundError("Potential Path Traversal detected")
        if input_data.startswith("<script>"):
            raise ValueError("XSS detected")
        if "DROP TABLE" in input_data.upper():
            raise ValueError("SQL Drop Command detected")
        if input_data.startswith("{") and input_data.endswith("}"):
            raise ValueError("JSON input detected")

        # Simulate random processing
        if "test@example.com" in input_data:
            raise RuntimeError("Simulated crash")

        print(f"✅ Processed successfully: '{input_data}'")
        log_fuzz_data(input_data, False, None)

    except Exception as e:
        print(f"⚠️ Crash detected: '{input_data}' - Error: {e}")
        log_fuzz_data(input_data, True, str(e))

if __name__ == "__main__":
    inputs = generate_test_inputs()
    for input_data in inputs:
        fuzz_target(input_data)
