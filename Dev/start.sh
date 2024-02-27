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

echo "Starting Django server..."
tmux new-session -d -s django_session
tmux send-keys -t django_session "source $VIRTUAL_ENV/bin/activate" Enter
# Send Django server command to a new window in the tmux session
tmux send-keys -t django_session "cd _server || exit" Enter
# Check if python3 command is available
if command -v python3 &>/dev/null; then
    tmux send-keys -t django_session "python3 manage.py runserver" Enter
# Check if python command is available
elif command -v python &>/dev/null; then
    tmux send-keys -t django_session "python manage.py runserver" Enter
else
    echo "Python interpreter not found. Please install Python."
    exit 1
fi
echo "Django server started."

echo "Starting Vue development server..."
# Create a new window for Vue development server
tmux new-session -d -s vue_session
# start the Vue development server
tmux send-keys -t vue_session "source $VIRTUAL_ENV/bin/activate" Enter
tmux send-keys -t vue_session "cd client || exit" Enter
tmux send-keys -t vue_session "npm run dev" Enter
echo "Vue development server started."

# Open the app in default browser (in the current terminal)
echo "Visit the backend at http://localhost:8000/api/user/create/"
echo "Visit the frontend at http://localhost:5173/static"
echo "Tmux sessions created:"
tmux ls
