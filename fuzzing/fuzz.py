import atheris
import sys
import logging
from targets.buggy_code import buggy_function  

logging.basicConfig(level=logging.INFO)

def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        logging.info(f"📝 Testing input: {repr(input_str)}")
        buggy_function(input_str)  # Run fuzzing input through target function
    except Exception as e:
        logging.error(f"❌ Fuzzing found a bug! Input: {repr(input_str)} | Error: {e}")
        raise  # Re-raise to let Atheris report it
    
def TestTwoInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        logging.info(f"📝 Testing input: {repr(input_str)}")
        buggy_function(input_str)  # Run fuzzing input through target function
    except Exception as e:
        logging.error(f"❌ Fuzzing found a bug! Input: {repr(input_str)} | Error: {e}")
        raise  # Re-raise to let Atheris report it

def main():
    atheris.Setup(["fuzz.py", "corpus"], TestTwoInput)  
    atheris.Setup(sys.argv, TestOneInput)   

    # atheris.instrument_all()
    atheris.Fuzz()



if __name__ == "__main__":
    main()
