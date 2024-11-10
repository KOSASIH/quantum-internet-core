#!/bin/bash

# generate_docs.sh
# Script to generate documentation for the project

set -e  # Exit immediately if a command exits with a non-zero status

echo "Generating documentation..."

# Activate the virtual environment
source venv/bin/activate

# Generate documentation using Sphinx
if [ ! -d "docs" ]; then
    echo "Creating documentation directory..."
    mkdir docs
    sphinx-quickstart docs
fi

# Build the documentation
cd docs
make html

echo "Documentation generated successfully! You can find it in the docs/_build/html directory."
