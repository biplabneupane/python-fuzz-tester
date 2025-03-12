import os
import math
import matplotlib.pyplot as plt

def calculate_entropy(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    if not data:
        return 0  # Empty file, zero entropy

    freq = {}
    for byte in data:
        freq[byte] = freq.get(byte, 0) + 1

    entropy = -sum((count / len(data)) * math.log2(count / len(data)) for count in freq.values())
    return entropy

def analyze_directory(directory):
    entropy_results = {}
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            entropy_results[filename] = calculate_entropy(file_path)
    
    return entropy_results

def plot_entropy(entropy_results):
    files = list(entropy_results.keys())
    entropy_values = list(entropy_results.values())

    plt.figure(figsize=(10, 5))
    plt.barh(files, entropy_values, color='skyblue')
    plt.xlabel("Entropy")
    plt.ylabel("Files")
    plt.title("Entropy Analysis of Fuzzing Inputs")
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.savefig("entropy_plot.png")  # Saves the plot as an image file

if __name__ == "__main__":
    directory = "./fuzzing_inputs"  # Change this to your actual directory
    entropy_results = analyze_directory(directory)
    
    for file, entropy in entropy_results.items():
        print(f"{file}: Entropy = {entropy:.4f}")

    plot_entropy(entropy_results)
