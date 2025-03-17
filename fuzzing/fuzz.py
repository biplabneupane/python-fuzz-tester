import hashlib
import os

CORPUS_DIR = "fuzzing_inputs/corpus"

def save_interesting_case(input_str):
    """Stores unique test cases for further analysis."""
    if not os.path.exists(CORPUS_DIR):
        os.makedirs(CORPUS_DIR)

    hash_value = hashlib.md5(input_str.encode()).hexdigest()
    file_path = os.path.join(CORPUS_DIR, f"case_{hash_value}.txt")

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(input_str)
        print(f"📝 Saved interesting test case: {file_path}")

def CombinedFuzzFunction(data):
    """Randomly selects a function to fuzz the input and saves interesting cases."""
    input_str = data.decode("utf-8", errors="ignore")
    random.choice([TestOneInput, TestTwoInput])(data)
    save_interesting_case(input_str)
