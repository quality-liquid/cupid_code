# Django + Vue

## Getting Started

Run `poetry install` in the Dev directory to make sure the poetry.lock file exists/is up to date.

------
## Django

In `_server`, create your own .env file. You can copy the data in the .env.example file 

DO NOT remove or rename the .env.example file!! Only copy from it!

Activate your shell using `poetry shell`

In `_server`, run `python manage.py makemigrations` and `python manage.py migrate`

------
## Vue
In `client`, run `npm install` to get all dependies. 

Make sure you do this anytime the package.json file is changed since node_modules will always be gitignored.

------
## Running the server

In one terminal, run `python mangae.py runserver` in `_server`
    
*Make sure you're in the poetry shell first*

In another terminal, run `npm run dev` in `client`

Visit the app at `http://localhost:8000`

------
## Additional Notes

VSCode will underline all imports and uses of imports in `_server` with yellow if your shell is not activated. This is okay! This is just how VSCode interprets the version management. It counts them as missing if you're coding w/o the shell management. If you want the lines gone then code with the shell active and use the quick fix to set it to the Poetry environment it will remove the underlines.

If you get any yellow unerlines in `client` then you likely have not updated your node_modules. Run `npm install` and it will solve that issue!