### Run Locally
Python Version: 3.9.7

Requirements:
```
sqlite3
```

### `db.py`
This file is used to connect to the Database.If the database does not exist, then it will be created and finally a database object will be returned.

### `seed.py`
In this file, I have created a table which will store user information.

### `api.py`
In this script, I have fetched data from the given api and validated the input date to have only future dates.

### `user.py`
In user.py file, I have written different methods to have the following functionality 
create new user, delete user, udpate user, read all user.

### `test_user.py`
In this file, I have written following unit tests.
Create new user -> In this function, I have written a logic for new user and for existing user. If user is already exists then it will show error, if not then it will create a new user.

Update user -> This will check that the existing user will updated or not, if user does not exists then it will show error.

Read all user, Check password, Delete user.

### `cli.py`
This file has the controlling logic for whole application.

```
which poetry
poetry install
poetry shell
python database/seed.py
python src/cli.py
```