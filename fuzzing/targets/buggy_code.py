# targets/buggy_code.py

def buggy_function(data):
    if len(data) > 5 and data[0] == ord('A'):
        raise ValueError("Crash triggered by fuzzing input!")
    return data[::-1]  # Reverse input as a dummy processing step
