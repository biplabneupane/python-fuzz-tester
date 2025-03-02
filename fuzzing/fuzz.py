import atheris
import sys
import logging
from targets.buggy_code import buggy_function  

logging.basicConfig(level=logging.INFO)

def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        logging.info(f"Testing input: {repr(input_str)}")  # Add logging
        buggy_function(input_str)  
    except Exception as e:
        logging.error(f"Fuzzing found a bug: {e}")
        raise RuntimeError(f"Fuzzing found a bug: {e}")

def main():
    atheris.Setup(sys.argv, TestOneInput)  
    atheris.instrument_all()
    atheris.Fuzz()

if __name__ == "__main__":
    main()
