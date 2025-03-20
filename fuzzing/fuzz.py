import random
import string
from datetime import datetime, timezone
from fuzzing.fuzz_logging import log_info, log_crash, log_fuzz_data

def generate_fuzz_input():
    """Generates various types of test cases."""
    test_cases = [
        "",  # Empty string
        "A" * 1000,  # Long string
        "".join(random.choices(string.ascii_letters + string.digits, k=20)),  # Random string
        "<script>alert('XSS')</script>",  # XSS attack vector
        "' OR 1=1 --",  # SQL Injection
        "../../etc/passwd",  # Path traversal
        '{"key": "value"}',  # Valid JSON
        '{"key": value}',  # Invalid JSON
        "∞",  # Unicode character
        "\x00\x01\x02\x03",  # Binary data
    ]
    return random.choice(test_cases)

def TestOneInput(input_str):
    """Function to process and test the input string."""
    try:
        log_info(f"📝 Testing input in TestOneInput: {repr(input_str)}")

        # Simulate processing
        if input_str == "":
            raise ValueError("Empty input detected")
        elif input_str.startswith("<script>"):
            raise RuntimeError("Potential XSS detected")
        elif "' OR " in input_str:
            raise RuntimeError("Potential SQL Injection detected")
        elif "../" in input_str:
            raise RuntimeError("Potential Path Traversal detected")
        elif input_str.startswith("{") and not input_str.endswith("}"):
            raise ValueError("Malformed JSON input")

        log_fuzz_data(input_str, crashed=0)  # Log non-crashing input

    except Exception as e:
        log_crash(input_str, str(e))  # Log crashing input

if __name__ == "__main__":
    sample_data = generate_fuzz_input()
    TestOneInput(sample_data)
