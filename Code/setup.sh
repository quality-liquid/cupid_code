#!/bin/bash

# Install Python dependencies using poetry
poetry install

# Create Django .env file
cp server/.env.example server/.env
echo "VAULT_PATH=$PWD/server/core/static/" >> server/.env

# Activate poetry shell
# poetry shell
echo "Continue"

# Apply Django migrations
cd server || exit
# Check if python3 command is available
if command -v poetry &>/dev/null; then
    poetry run python3 manage.py makemigrations
    poetry run python3 manage.py migrate
# Check if python command is available
elif command -v python &>/dev/null; then
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
else
    echo "Python interpreter not found. Please install Python."
    exit 1
fi

# Navigate to Vue client directory
cd ../client || exit

# Install npm dependencies
npm install

# Go back to Code directory
cd .. || exit