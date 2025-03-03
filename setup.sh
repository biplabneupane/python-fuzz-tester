#!/bin/bash

source fuzz_env/bin/activate
echo " Running the fuzzer..."
python3 fuzzing/fuzz.py
