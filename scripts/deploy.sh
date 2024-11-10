#!/bin/bash

# deploy.sh
# Deployment script for production

set -e  # Exit immediately if a command exits with a non-zero status

echo "Deploying the application to production..."

# Activate the virtual environment
source venv/bin/activate

# Pull the latest code from the repository
echo "Pulling the latest code from the repository..."
git pull origin main

# Install any new dependencies
echo "Installing new dependencies..."
pip install -r requirements.txt

# Run database migrations (if applicable)
# echo "Running database migrations..."
# python manage.py migrate

# Restart the application service (assuming a systemd service)
echo "Restarting the application service..."
sudo systemctl restart quantum_app.service

echo "Deployment completed successfully!"
