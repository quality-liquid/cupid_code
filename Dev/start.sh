#!/bin/bash

# Run Django server
echo "Starting Django server..."
python manage.py runserver

# Run Vue development server
echo "Starting Vue development server..."
npm run dev

# Open the app in default browser
echo "Visit the app at http://localhost:8000"
