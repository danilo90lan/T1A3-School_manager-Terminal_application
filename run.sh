#!/bin/bash
python3 -m venv venv

# Activate the environment
source venv/bin/activate

# Install the dependecies from the requirements.txt
pip install -r requirements.txt

# Run the main application
python src/main.py

# Deactivate the virtual environment
deactivate