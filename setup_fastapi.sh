#!/bin/bash

# Define environment name
VENV_DIR="fastapi_env"

# 1. Ensure system-level dependencies are installed (Ubuntu specific)
echo "Checking for system dependencies..."
if ! dpkg -s python3-venv python3-pip >/dev/null 2>&1; then
    echo "Installing python3-venv and python3-pip..."
    sudo apt update
    sudo apt install -y python3-venv python3-pip
else
    echo "System dependencies already met."
fi

# 2. Create the virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment '$VENV_DIR'..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment '$VENV_DIR' already exists."
fi

# 3. Activate the environment
# Use 'source' to ensure it's activated in the current subshell
source "$VENV_DIR/bin/activate" || { echo "Failed to activate venv"; exit 1; }

# 4. Install FastAPI within the venv
# Note: Inside the venv, you can use 'pip' directly
if ! python3 -c "import fastapi" &> /dev/null; then
    echo "FastAPI not found in venv. Installing..."
    pip install --upgrade pip
    pip install "fastapi[standard]"
else
    echo "FastAPI is already installed in '$VENV_DIR'."
fi

echo "-----------------------------------------------"
echo "Setup complete. To start using it, run:"
echo "source $VENV_DIR/bin/activate"

