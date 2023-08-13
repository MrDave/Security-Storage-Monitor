# Security Storage Monitor

Web interface for monitoring users of a storage: their passcards and entrance activity

This project is designed for using with a specific database and won't run properly without access to the same database, however the code can be viewed freely to see how the project works
## How to install

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Project and database settings are stored in `project/settings.py` while sensitive data (database's host, user, password and the secret key) as well as the debug boolean are stored in `.env` file.

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