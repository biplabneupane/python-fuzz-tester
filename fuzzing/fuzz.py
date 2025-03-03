import atheris
import sys
import logging
import random
from targets.buggy_code import buggy_function  

logging.basicConfig(level=logging.INFO)

def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        logging.info(f"📝 Testing input in TestOneInput: {repr(input_str)}")
        buggy_function(input_str)
    except Exception as e:
        logging.error(f"❌ Fuzzing found a bug! Input: {repr(input_str)} | Error: {e}")
        raise

def TestTwoInput(data):
    """Another fuzz function to test different cases."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        logging.info(f"📝 Testing input in TestTwoInput: {repr(input_str)}")
        buggy_function(input_str)
    except Exception as e:
        logging.error(f"❌ Fuzzing found a bug! Input: {repr(input_str)} | Error: {e}")
        raise

def CombinedFuzzFunction(data):
    """Randomly selects a function to fuzz the input."""
    random.choice([TestOneInput, TestTwoInput])(data)

def main():
    atheris.Setup(sys.argv, CombinedFuzzFunction)  
    atheris.Fuzz()

if __name__ == "__main__":
    main()
