#!/bin/bash

# setup_environment.sh
# Script to set up the development environment for the quantum computing application

set -e  # Exit immediately if a command exits with a non-zero status

echo "Setting up the development environment..."

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install Python and pip
echo "Installing Python and pip..."
sudo apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# Install additional system dependencies (if any)
echo "Installing additional system dependencies..."
# Example: sudo apt-get install -y libboost-all-dev

echo "Development environment setup complete!"
