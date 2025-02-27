import atheris
import sys
from targets.buggy_code import buggy_function  # Import function to test

def TestOneInput(data):
    try:
        buggy_function(data)  # Run fuzzing input through target function
    except Exception as e:
        raise RuntimeError(f"Fuzzing found a bug: {e}")

def main():
    atheris.instrument_all()
    atheris.Fuzz()

if __name__ == "__main__":
    main()
