#!/bin/bash

# Ensure pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "pytest is not installed. Installing pytest..."
    pip install pytest
fi

# Run pytest on the main script
pytest --maxfail=1 --disable-warnings -q