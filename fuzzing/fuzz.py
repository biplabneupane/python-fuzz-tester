import random
from fuzzing.fuzz_logging import log_info, log_crash, log_fuzz_data

def TestOneInput(input_data, category="unknown"):
    """Tests a given input and logs results."""
    try:
        if not isinstance(input_data, str):
            raise TypeError("Input must be a string")

        # Simulate potential crashes for fuzz testing
        if random.choice([False, False, False, True]):  # 25% crash rate
            raise ValueError("Simulated crash")

        log_info(f"✅ Processed successfully: {repr(input_data)}")
        log_fuzz_data(input_data, crashed=0)  # Log as non-crashing

    except Exception as e:
        log_crash(input_data or "None", str(e))  # Handle None inputs
        log_info(f"⚠️ Error logged for input: {repr(input_data)}")


# Test cases
test_inputs = [
    ("Hello, world!", "valid"),
    ("12345", "valid"),
    ("test@example.com", "valid"),
    ("", "edge"),  # Empty input
    (" " * 1000, "edge"),  # Large whitespace input
    ("特殊字符", "edge"),  # Unicode characters
    (None, "invalid"),  # NoneType input
]

for input_str, category in test_inputs:
    log_info(f"📝 Testing {category} input: {repr(input_str)}")
    TestOneInput(input_str, category)
