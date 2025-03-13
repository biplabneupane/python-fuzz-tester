from targets.buggy_code import buggy_function
from fuzz_logging import log_info, log_crash

def fuzz_target(data):
    """Fuzzing target wrapper for buggy_function"""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        log_info(f"Running fuzz_target with input: {input_str}")
        buggy_function(input_str)
    except Exception as e:
        log_crash(input_str, str(e))
