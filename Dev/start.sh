#!/bin/bash

cd _server || exit

# Run Django server
echo "Starting Django server..."
# Check if python3 command is available
if command -v python3 &>/dev/null; then
    python3 manage.py runserver
# Check if python command is available
elif command -v python &>/dev/null; then
    python manage.py runserver
else
    echo "Python interpreter not found. Please install Python."
    exit 1
fi

cd ../client || exit
# Run Vue development server
echo "Starting Vue development server..."
npm run dev

# Open the app in default browser
echo "Visit the app at http://localhost:8000"
