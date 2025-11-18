## Running tests
The process of running tests will be the same as the previous team. We will have to update the tests themselves, but they will follow the same process to run.

### Unit tests  

To set up the environment, navigate to the `Code/` directory and use `poetry` to install the dependencies situated in the `poetry.lock` file. Use the following command to do so:

```poetry install```

To run a unit test using Django's framework, navigate to the `Code/server/` directory, where `manage.py` resides. The tests we wrote are for the `api` application. Use the following command to run the tests:

```python manage.py test api.tests.unit_tests.cupid_tests```

### Automated system tests

One-time setup:

1. Follow the instructions in [Documentation/Manual/installation_manual.md](../../Manual/installation_manual.md) to get poetry set up.
    - The only dependency you really need is selenium, but if you have the project as a whole set up, then you will have selenium
2. Migrate the database (as described in [Code/README.md](../../../Code/README.md)) so you have a fresh database. The tests all rely on a fresh database, so each one restores a backup before running. To ensure there is a backup copy `Code/server/db.sqlite3` to `Code/server/db_backup.sqlite3`
3. Set up your options in `Code/selenium/options.conf`
    - `chrome=true` will use chrome, otherwise firefox will be used
    - `headless=true` will cause the tests to run headless(no browser window) otherwise you will see the browser

Every-time:

1. Ensure the server is up and running for the frontend and backend.[Code/README.md](../../../Code/README.md)
2. Navigate to [Code/selenium](../../../Code/selenium)
3. Ensure you have access to selenium, run `poetry shell` if using poetry.
4. Run all tests with `python run_tests.py`, or run specific tests with `python test_*.py`

### Manual system test

Use-case: As a dater, create a gig. As a cupid, complete the gig and rate the dater.

Dater:

0. Ensure the server is up and running for the frontend and backend.[Code/README.md](../../../Code/README.md)
0. Sign in as a dater (use a new container/profile, incognito/private, or logout first)
    - username: bob@cupidcode.com
    - password: password
0. Click on "Add Cash" and check your balance
0. Use the side panel to navigate the the "gigs" page
0. Add a gig with a budget lower than your balance.

Cupid:

0. Sign in as a cupid
    - username: really@me.com
    - passowrd: password
0. Click on "profile" and check your balance
0. Click the "find gigs" link on the home page
0. Claim a gig.
0. Mark the gig as complete.
0. Use the sidepanel to navigate to "Profile" and check that the balance has increased
0. Use the sidepanel to navigate to "Gigs Completed"
0. Click "Rate Dater"
0. Enter a message describing your rating, and select a heart count.
0. Click "Send"

Verify results:

0. Log back in as the dater
0. Click on "Add Cash" and verify the balance has decreased
0. Use the sidebar to navigate to "Feedback"
0. You should see your new review at the bottom of the list.
