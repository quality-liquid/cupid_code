#!/bin/bash

# Install Python dependencies using poetry
poetry install

# Make the poetry env explicity use the python3.14 interpreter
poetry env use python3.14

# Create Django .env file
if [ -f "server/.env" ]; then
    echo "Server .env already exists. Skipping creation..."
else
    cp server/.env.example server/.env
    echo "VAULT_PATH=$PWD/server/core/static/" >> server/.env
fi

# Create Client .env file
if [ -f "client/.env" ]; then
    echo "Client .env already exists. Skipping creation..."
else
    cp client/.env.example client/.env
fi

# Apply Django migrations
# cd server || exit
# # Check if python3 command is available
# if command -v poetry run python &>/dev/null; then
#     poetry run python3 manage.py makemigrations
#     poetry run python3 manage.py migrate
# # Check if python command is available
# elif command -v python &>/dev/null; then
#     poetry run python manage.py makemigrations
#     poetry run python manage.py migrate
# else
#     echo "Python interpreter not found. Please install Python."
#     exit 1
# fi

# # Navigate to Vue client directory
# cd ../client || exit

# # Install npm dependencies, `npm ci` is better for CI/CD. See `npm help ci` (the man page)
# npm ci

# # Go back to Code directory
# cd .. || exit

# # Print help message to remind developer to add in API keys
# TODO_MSG="\033[1;31mTODO: Add your API keys to the %s .env file to finish setup!"
# printf "\n\n$TODO_MSG" "server"
# printf "\n$TODO_MSG\n\n" "client"