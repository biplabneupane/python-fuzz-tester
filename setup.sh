#!/bin/bash

# Exit on error
set -e  

# Create and activate virtual environment
python3 -m venv fuzz_env
source fuzz_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required dependencies
pip install atheris

# Success message
echo "✅ Setup complete! Run 'source fuzz_env/bin/activate' to activate the virtual environment."
