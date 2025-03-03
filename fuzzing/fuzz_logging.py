import atheris
import sys
import logging
import os
from targets.buggy_code import buggy_function  

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "fuzzing.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        logging.info(f"📝 Testing input: {repr(input_str)}")
        buggy_function(input_str)  # Run fuzzing input through target function
    except Exception as e:
        crash_filename = os.path.join(LOG_DIR, f"crash-{hash(input_str)}.txt")
        with open(crash_filename, "w") as f:
            f.write(f"Input: {repr(input_str)}\nError: {str(e)}\n")
        logging.error(f"❌ Fuzzing found a bug! Crash saved in {crash_filename}")
        raise  # Re-raise to let Atheris report it

def main():
    atheris.Setup(sys.argv, TestOneInput)  
    atheris.Fuzz()

if __name__ == "__main__":
    main()
