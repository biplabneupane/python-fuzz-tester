import atheris
import time
import sys
import random
from targets.buggy_code import buggy_function  
from fuzz_logging import log_info, log_error, log_crash  # Import logging functions

def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        log_info(f"📝 Testing input in TestOneInput: {repr(input_str)}")
        buggy_function(input_str)
    except Exception as e:
        log_crash(input_str, str(e))  # Log crashes separately
        raise  # Allow atheris to detect the crash

def TestTwoInput(data):
    """Another fuzz function to test different cases."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        log_info(f"📝 Testing input in TestTwoInput: {repr(input_str)}")
        buggy_function(input_str)
    except Exception as e:
        log_crash(input_str, str(e))
        raise

def CombinedFuzzFunction(data):
    """Randomly selects a function to fuzz the input."""
    random.choice([TestOneInput, TestTwoInput])(data)

def main():
    atheris.instrument_all()
    atheris.Setup(sys.argv, CombinedFuzzFunction)
    start_time = time.time()
    timeout = 60  # Run for 60 seconds
    while time.time() - start_time < timeout:
        atheris.Fuzz()

if __name__ == "__main__":
    main()
