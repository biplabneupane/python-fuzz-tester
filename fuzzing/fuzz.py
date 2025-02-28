import atheris
import sys
from targets.buggy_code import buggy_function  # Import function to test

def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        # Convert bytes to string safely
        input_str = data.decode("utf-8", errors="ignore")
        buggy_function(input_str)  # Run fuzzing input through target function
    except Exception as e:
        raise RuntimeError(f"Fuzzing found a bug: {e}")

def main():
    atheris.Setup(sys.argv, TestOneInput)  # Correct setup for Atheris
    atheris.instrument_all()
    atheris.Fuzz()

if __name__ == "__main__":
    main()
