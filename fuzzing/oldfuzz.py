from fuzzing.fuzz_logging import log_info, log_crash, log_fuzz_data
from fuzzing.targets.buggy_code import buggy_function


def TestOneInput(data):
    """Fuzz target function with input data."""
    try:
        input_str = data.decode("utf-8", errors="ignore")
        log_info(f"📝 Testing input in TestOneInput: {repr(input_str)}")

        log_fuzz_data(input_str, crashed=0)  # Log input as non-crashing first
        buggy_function(input_str)
    
    except Exception as e:
        log_crash(input_str, str(e))  # Log as crashing
        raise  
if __name__ == "__main__":
    sample_data = b"test input"
    TestOneInput(sample_data)
