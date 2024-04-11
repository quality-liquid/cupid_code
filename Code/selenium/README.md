# Setup
You will need to freshly migrate the db and then copy `Code/server/db.sqlite3` to `Code/server/db_backup.sqlite`. The tests rely on a freshly migrated database, so they routinely replace the db with the backup

You will find `options.conf` in this directory. Simply set chrome to `true` if you want to use chrome instead of firefox. Similarly set headless to `true` if you don't want to see the web broswer, which should lead to faster tests.

# Running Tests
Run all tests with `python run_tests.py` 

Run specific tests with `python test_x.py`

# Common Problems
If you are getting errors about unexpected data, you may have a bad db. Make sure you have a freshly migrated db. If you have on stored in `Code/server/db_backup.sqlite3` you can run `python utils.py` and it will invoke `db_restore()`
