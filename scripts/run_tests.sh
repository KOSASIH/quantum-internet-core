#!/bin/bash

# run_tests.sh
# Script to run all tests in the project

set -e  # Exit immediately if a command exits with a non-zero status

echo "Running all tests..."

# Activate the virtual environment
source venv/bin/activate

# Run unit tests
echo "Running unit tests..."
python -m unittest discover -s tests/unit -p "*.py"

# Run integration tests
echo "Running integration tests..."
python -m unittest discover -s tests/integration -p "*.py"

# Run performance tests
echo "Running performance tests..."
python -m unittest discover -s tests/performance -p "*.py"

echo "All tests completed successfully!"
