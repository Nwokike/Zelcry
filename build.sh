#!/usr/bin/env bash
# Render.com build script for Zelcry
# Exits on error
set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate

echo "Seeding cryptocurrency data..."
python manage.py seed_crypto_data

echo "Build completed successfully!"
