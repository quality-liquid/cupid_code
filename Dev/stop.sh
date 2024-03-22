#!/bin/bash

# Get list of tmux sessions
sessions=$(tmux ls | cut -d ':' -f 1)

# Loop through each session
for session in $sessions; do
    # Send "exit" to each pane in the session to gracefully terminate processes
    tmux send-keys -t "$session" C-c
done

# Kill all tmux sessions
tmux kill-server
echo "Tmux sessions killed"
tmux ls