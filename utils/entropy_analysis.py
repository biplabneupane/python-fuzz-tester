import math
from collections import Counter

def calculate_entropy(hex_string):
    """Calculate Shannon entropy of a hex string."""
    byte_counts = Counter(hex_string)  # Count occurrences of each byte
    total_bytes = len(hex_string)
    
    entropy = -sum((count / total_bytes) * math.log2(count / total_bytes) for count in byte_counts.values())
    
    return entropy

# Example usage:
hex_data = "ffffffffffffff096868686868686868686868686868686868686868686868686868686868686868"
entropy_value = calculate_entropy(hex_data)
print(f"Entropy: {entropy_value:.4f}")
