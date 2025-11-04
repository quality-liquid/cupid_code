#!/bin/bash

# Install Python dependencies using poetry
poetry install

# Create Django .env file
cp server/.env.example server/.env
echo "VAULT_PATH=$PWD/server/core/static/" >> server/.env

# Create Client .env file
cp client/.env.example client/.env

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

# Install npm dependencies, `npm ci` is better for CI/CD. See `npm help ci` (the man page)
npm ci

# Go back to Code directory
cd .. || exit

# Print help message to remind developer to add in API keys
TODO_MSG="\033[1;31mTODO: Add your API keys to the %s .env file to finish setup!"
printf "\n\n$TODO_MSG" "server"
printf "\n$TODO_MSG\n\n" "client"