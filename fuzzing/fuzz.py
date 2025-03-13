import atheris
import sys
import random
import multiprocessing
import os
from targets.buggy_code import buggy_function  
from fuzz_logging import log_info, log_crash  # Import logging functions

def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        log_info(f"📝 Testing input in TestOneInput: {repr(input_str)}")
        buggy_function(input_str)
    except Exception as e:
        log_crash(input_str, str(e))
        raise  

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

def run_fuzzer():
    """Runs the fuzzing process."""
    atheris.instrument_all()
    atheris.Setup(sys.argv, CombinedFuzzFunction)
    atheris.Fuzz()

def TestFromFile(directory):
    """Reads all text files in a directory and runs fuzzing functions."""
    if not os.path.exists(directory):
        print(f"⚠️ Warning: Directory '{directory}' not found. Skipping file-based fuzzing.")
        return
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            print(f"📂 Running fuzzing from file: {filepath}")
            try:
                with open(filepath, "rb") as f:
                    inputs = f.readlines()
                for data in inputs:
                    data = data.strip()
                    if data:
                        CombinedFuzzFunction(data)
            except FileNotFoundError:
                print(f"⚠️ Warning: File '{filepath}' not found. Skipping...")

def main():
    """Main function to run both file-based and random fuzzing."""
    timeout = 60  # Set timeout in seconds
    input_dir = "fuzzing_inputs"  # Directory containing input test cases

    print("📂 Running fuzzing from input files...")
    TestFromFile(input_dir)  # Process all test files first

    print("🎲 Running random fuzzing with Atheris...")
    p = multiprocessing.Process(target=run_fuzzer)
    p.start()
    p.join(timeout)  # Allow it to run for the set duration

    if p.is_alive():
        print("⏳ Timeout reached. Stopping the fuzzer...")
        p.terminate()
        p.join()

if __name__ == "__main__":
    main()
