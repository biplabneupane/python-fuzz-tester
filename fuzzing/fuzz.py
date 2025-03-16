import atheris
import sys
import random
import multiprocessing
import time
import json
from targets.buggy_code import buggy_function
from fuzz_logging import log_info, log_crash

# Track statistics
STATS_FILE = "logs/stats.json"
stats = {"total_tests": 0, "crashes": 0, "start_time": time.time()}


def save_stats():
    """Save current statistics to a file."""
    stats["elapsed_time"] = round(time.time() - stats["start_time"], 2)
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)


def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        log_info(f"📝 Testing input: {repr(input_str)}")
        buggy_function(input_str)
    except Exception as e:
        log_crash(input_str, str(e))
        stats["crashes"] += 1
    finally:
        stats["total_tests"] += 1
        save_stats()


def run_fuzzer():
    """Runs the fuzzing process."""
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


def TestFromFile(filename):
    """Reads inputs from a file, shuffles, and runs fuzzing."""
    try:
        with open(filename, "rb") as f:
            inputs = f.readlines()

        random.shuffle(inputs)  # Shuffle for better coverage

        for data in inputs:
            data = data.strip()
            if data:
                TestOneInput(data)
    except FileNotFoundError:
        print(f"⚠️ Warning: File '{filename}' not found. Running random fuzzing only.")


def main():
    """Main function to run both file-based and random fuzzing."""
    timeout = 60  # Set timeout in seconds
    input_file = "fuzzing_inputs.txt"

    print(f"📂 Running fuzzing from file: {input_file}")
    TestFromFile(input_file)

    print("🎲 Running random fuzzing with Atheris...")
    p = multiprocessing.Process(target=run_fuzzer)
    p.start()
    p.join(timeout)

    if p.is_alive():
        print("⏳ Timeout reached. Stopping the fuzzer...")
        p.terminate()
        p.join()

    save_stats()  # Save final statistics


if __name__ == "__main__":
    main()
