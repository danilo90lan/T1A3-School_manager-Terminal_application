#!/bin/bash

# Check if the number of arguments is more than 2
if [ "$#" -gt 4 ]; then
    echo "Error: Too many arguments provided. Maximum 2 arguments allowed."
    exit 1
fi

# Check if Python 3 is available
if [[ -x "$(command -v python3)" ]]; then
    # Check Python 3 version
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]; then
    
        # Create virtual environment
        python3 -m venv virtualenv

        # Activate the virtual environment
        source virtualenv/bin/activate

        # Install dependencies
        pip install -r requirements.txt

        # Run the main application
        # python3 src/main.py $1 $2 $3 $4

        # Or you can run the script like this, same thing
        python3 src/main.py $@

        # Deactivate the virtual environment
        deactivate
    else
        echo "You have the wrong version of Python. Install Python 3" >&2
        echo "To install Python, check out https://installpython3.com/" >&2
    fi
else
    echo "Python 3 is not installed." >&2
    echo "To install Python, check out https://installpython3.com/" >&2
fi