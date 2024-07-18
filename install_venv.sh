#!/bin/bash

# Check if venv is installed
# it runs the command but without displaying any output
# >:

# This is the output redirection operator. It directs the standard output (stdout) of a command to a file or another output destination.
# /dev/null:

# /dev/null is a special file in Unix-like systems that discards all data written to it. It is often used to suppress output.
# 2>&1:
# Redirects the standard error (stderr) of the venv --help command to the same place as the standard output (stdout), which is /dev/null.
python3 -m venv --help > /dev/null 2>&1

# checks the exit status ($?) of the previous command (python3 -m venv --help)
# If the exit status is not 0, it proceeds to install venv using sudo apt-get
# update and sudo apt-get install -y python3-venv

# la sintassi e' if [ condtion_with_space_at_the_tart_and_end ]; then
# oppure f [ condtion_with_space_at_the_tart_and_end ]
# then
if [[ $? == 0 ]]; then
    echo "venv is already installed."
else
    echo "venv is not installed. Installing venv..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
    python3 -m venv --help > /dev/null 2>&1
    echo "venv was successfully installed."
fi