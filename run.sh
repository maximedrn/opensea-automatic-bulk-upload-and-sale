#!/bin/bash

# Set the Python path.
PYTHON_PATH="python3"

# Set the environment name.
ENV_NAME="env"

# Create a Python environment.
if [ ! -d "$ENV_NAME" ]; then
    "$PYTHON_PATH" -m venv "$ENV_NAME"
fi

# Activate the Python environment.
source "$ENV_NAME/bin/activate"

# Install requirements.
$PYTHON_PATH -m pip install -r requirements.txt

# Run the main.py file.
$PYTHON_PATH main.py

# Deactivate the Python environment.
deactivate
