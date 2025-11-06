#!/bin/bash

# Install Python dependencies using poetry
poetry install

# Make the poetry env explicity use the python3.14 interpreter
poetry env use python3.14

ADD_SERVER_API_KEY="false"
ADD_CLIENT_API_KEY="false"

# Create Django .env file
if [ -f "server/.env" ]; then
    echo "Server .env already exists. Skipping creation..."
    if grep -q 'STRIPE_SECRET_KEY=""' server/.env || grep -q 'STRIPE_WEBHOOK_SECRET=""' server/.env; then
        ADD_SERVER_API_KEY="true"
    fi
else
    cp server/.env.example server/.env
    sed -i.bak "s|^VAULT_PATH=.*|VAULT_PATH=\"$PWD/server/core/static/\"|" server/.env
    rm server/.env.bak
    ADD_SERVER_API_KEY="true"
fi

# Create Client .env file
if [ -f "client/.env" ]; then
    echo "Client .env already exists. Skipping creation..."
    if grep -q 'VITE_STRIPE_PUBLISHABLE_KEY=""' client/.env; then
        ADD_CLIENT_API_KEY="true"
    fi
else
    cp client/.env.example client/.env
    ADD_CLIENT_API_KEY="true" 
fi

# Apply Django migrations
cd server || exit
# Check if python3 command is available
if command -v poetry run python &>/dev/null; then
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
TODO_MSG="\033[31mTODO: One or more API keys in the %s .env file are not set, please set keys to finish setup!"

if [ $ADD_SERVER_API_KEY = "true" ]; then
    printf "\n$TODO_MSG\n" "server"
fi

if [ $ADD_CLIENT_API_KEY = "true" ]; then
    printf "\n$TODO_MSG\n" "client"
fi