#!/usr/bin/env bash
# Build script for production deployment
# Runs during deployment to prepare the application

set -o errexit  # Exit on error

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate

echo "Seeding cryptocurrency data..."
python manage.py seed_crypto_data || echo "Seed data already exists or failed"

echo "Build complete!"
