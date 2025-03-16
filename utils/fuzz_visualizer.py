import json
import matplotlib.pyplot as plt
import os

STATS_FILE = "logs/stats.json"
OUTPUT_IMAGE = "logs/fuzz_progress.png"

def plot_fuzzing_progress():
    """Reads stats and generates a fuzzing progress graph."""
    if not os.path.exists(STATS_FILE):
        print("⚠️ No stats file found. Run the fuzzer first!")
        return

    with open(STATS_FILE, "r", encoding="utf-8") as f:
        stats = json.load(f)

    # Extract data
    total_tests = stats.get("total_tests", 0)
    elapsed_time = stats.get("elapsed_time", 0)

    # Plot results
    plt.figure(figsize=(6, 4))
    plt.bar(["Total Tests", "Elapsed Time (s)"], [total_tests, elapsed_time], color=['blue', 'red'])
    plt.title("Fuzzing Progress Overview")
    plt.xlabel("Metric")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    
    # Save the plot
    plt.savefig(OUTPUT_IMAGE)
    plt.show()
    print(f"📊 Fuzzing progress graph saved at: {OUTPUT_IMAGE}")

if __name__ == "__main__":
    plot_fuzzing_progress()
