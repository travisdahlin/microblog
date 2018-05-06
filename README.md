# Microblog
A demo python flask web application.
## Setup
- Clone the repository
- Create a virtual environment
```bash
$ python3 -m venv venv
```
- Activate the virtual environment
```bash
$ source venv/bin/activate 
```
- Install flask
```bash
$  pip install flask
```
- Install flask-wtf
```bash
$ pip install flask-wtf
```
 - Install flask-sqlalchemy
 ```bash
 $ pip install flask-sqlalchemy
 ```
 - Install flask-migrate
 ```bash
 $ pip install flask-migrate
 ```
- Set the FLASK-APP environment variable.
```bash
$ export FLASK_APP=microblog.py
```
- Initialize the database
```bash
$ flask db init
```
- Start the application
```bash
$ flask run
```