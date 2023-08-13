# Security Storage Monitor

Web interface for monitoring users of a storage: their passcards and entrance activity

This project is designed for using with a specific database and won't run properly without access to the same database, however the code can be viewed freely to see how the project works
## How to install

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Project and database settings are stored in `project/settings.py` while sensitive data as well as the debug boolean are stored in `.env` file (see Environment variables subsection).

### Environment variables

For the project to work correctly, several environmental variables have to be set in `.env` file: 

- `DB_HOST` - which host to use when connecting to the database
- `DB_PORT` - the port to use when connecting to the database
- `DB_NAME` - the name of the database to use
- `DB_USER` - the username to use when connecting to the database
- `DB_PASSWORD` - the password to use when connecting to the database
- `SECRET_KEY` - a secret key for a particular Django installation
- `ALLOWED_HOSTS` - a list of strings representing the host/domain names that this Django site can serve

Details about each setting can be found in [Django documentation](https://docs.djangoproject.com/en/4.2/ref/settings/).

Optional variable `DEBUG` can be included to toggle debugging mode:
```
DEBUG = True
```

## How to run

To set up the server, run
```commandline
python manage.py runserver 0.0.0.0:8000
```
Connect to `127.0.0.1:8000` or `localhost:8000` via browser

There you will find a list of active user passcards with options to view their visit history or to view current visitors in the storage
![Active passcards](https://i.imgur.com/Ad0SV01.png "Active passcards")  
![Current visitor](https://i.imgur.com/jml4cel.png "Current visitor")  
![User's visit history](https://i.imgur.com/mStWZui.png "User's visit history")

## Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).