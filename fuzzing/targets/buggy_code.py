def buggy_function(input_str):
    if "CRASH" in input_str:
        raise ValueError("Forced crash for testing purposes!")  # Force a crash
    return input_str[::-1]  # Normal behavior: reverse the string
