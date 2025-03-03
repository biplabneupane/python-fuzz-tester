#!/bin/bash

# Exit on error
set -e  

# Activate virtual environment
source fuzz_env/bin/activate

# Run the fuzzer and store logs
mkdir -p logs
python3 fuzz.py | tee logs/fuzz.log

echo "✅ Fuzzing complete! Check logs in logs/fuzz.log."
