#!/bin/bash

# Check if venv is installed
python3 -m venv --help > /dev/null 2>&1

# checks the exit status ($?) of the previous command (python3 -m venv --help)
# If the exit status is not 0, it proceeds to install venv using sudo apt-get
# update and sudo apt-get install -y python3-venv
if [ $? -eq 0 ]; then
    echo "venv is already installed."
else
    echo "venv is not installed. Installing venv..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
    python3 -m venv --help > /dev/null 2>&1
    echo "venv was successfully installed."
fi