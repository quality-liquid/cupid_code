# Cupid Code Start Guide

## Automated Cupid Code Setup

### Do once

1. Make sure you have installed poetry, npm, python, and tmux
2. make sure you are in the Dev directory
3. Run `poetry install` in the Dev directory to make sure the poetry.lock file exists/is up to date.
4. Run `npm install` in the client directory to make sure current npm packages are installed
5. Run `chmod +x setup.sh start.sh stop.sh restart.sh` to make the shell scripts executable
6. run `./setup.sh` to install poetry, install npm_modules, create the .env file, install python dependencies, and create the database

### Running the server

After the setup is complete, you can
- run `./start.sh` to start the django server and the vue.js middleware
- run `./stop.sh` to stop the django server and the vue.js middleware
- run `./restart.sh` to restart the django server and the vue.js middleware
- run `./setup.sh` to reinstall the project if changes are made to the .env file or the poetry.lock file

### Tmux Commands
- `tmux ls` to see what sessions are running
- `tmux kill-session -t my_session` to kill the session
- `tmux a -t my_session` to attach to the session
- `Ctrl+ b d or Ctrl+ b :detach` Detach from currently attached session 

-------------

## Manual Cupid Code Setup

### Getting Started

Run `poetry install` in the Dev directory to make sure the poetry.lock file exists/is up to date.

Run `npm install` in the client directory to make sure current npm packages are installed

### Django

In `_server`, create your own .env file. You can copy the data in the .env.example file 

DO NOT remove or rename the .env.example file!! Only copy from it!

Activate your shell using `poetry shell`

In `_server`, run `python manage.py makemigrations` and `python manage.py migrate`

### Vue
In `client`, run `npm install` to get all dependies. 

Make sure you do this anytime the package.json file is changed since node_modules will always be gitignored.

### Running the server

In one terminal, run `python mangae.py runserver` in `_server`
    
*Make sure you're in the poetry shell first*

In another terminal, run `npm run dev` in `client`

Visit the app at `http://localhost:8000`

### Additional Notes

VSCode will underline all imports and uses of imports in `_server` with yellow if your shell is not activated. This is okay! This is just how VSCode interprets the version management. It counts them as missing if you're coding w/o the shell management. If you want the lines gone then code with the shell active and use the quick fix to set it to the Poetry environment it will remove the underlines.

If you get any yellow underlines in `client` then you likely have not updated your node_modules. Run `npm install` and it will solve that issue!