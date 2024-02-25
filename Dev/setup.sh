#!/bin/bash

# Navigate to Dev directory
cd Dev || exit

# Install Python dependencies using poetry
poetry install

# Create Django .env file
cp _server/.env.example _server/.env

# Activate poetry shell
poetry shell

# Apply Django migrations
cd _server || exit
python manage.py makemigrations
python manage.py migrate

# Navigate to Vue client directory
cd ../client || exit

# Install npm dependencies
npm install