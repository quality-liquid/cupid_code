#!/bin/bash

if ! command -v tmux &>/dev/null; then
    echo "tmux not found. Please install tmux."
    echo "For Ubuntu/Debian: apt install tmux"
    echo "For Fedora: dnf install tmux"
    echo "For macOS: brew install tmux"
    echo "Once you have it run tmux -V to check the version."
    echo "Then you can run this script again."
    exit 1
fi

# Start a new tmux session named "my_session"
tmux new-session -d -s my_session

# Send Django server command to a new window in the tmux session
tmux send-keys -t my_django_session "cd _server || exit" Enter
tmux send-keys -t my_django_session "echo 'Starting Django server...'" Enter

# Check if python3 command is available
if command -v python3 &>/dev/null; then
    tmux send-keys -t my_django_session "python3 manage.py makemigrations" Enter
    tmux send-keys -t my_django_session "python3 manage.py migrate" Enter
    tmux send-keys -t my_django_session "python3 manage.py runserver" Enter
# Check if python command is available
elif command -v python &>/dev/null; then
    tmux send-keys -t my_django_session "python manage.py makemigrations" Enter
    tmux send-keys -t my_django_session "python manage.py migrate" Enter
    tmux send-keys -t my_django_session "python manage.py runserver" Enter
else
    echo "Python interpreter not found. Please install Python."
    exit 1
fi

# Create a new window for Vue development server
tmux new-window -t my_vue_session
tmux send-keys -t my_vue_session "cd ../client || exit" Enter
tmux send-keys -t my_vue_session "echo 'Starting Vue development server...'" Enter
tmux send-keys -t my_vue_session "npm run dev" Enter

# Open the app in default browser (in the current terminal)
echo "Visit the app at http://localhost:8000"
echo "Tmux sessions created:"
tmux ls