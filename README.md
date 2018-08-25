# Microblog

A demo python flask web application.

## Setup

### Init

- Clone the repository
- Create a virtual environment
- Activate the virtual environment

**Linux/Mac**

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

**Windows**

```ps
> python -m venv venv
> .\venv\Scripts\activate
```

### Install libraries

- Install flask
- Install flask-wtf
- Install flask-sqlalchemy
- Install flask-migrate
- Install flask-login

```bash
$ pip install -r requirements.txt
```

### Configure environment

- Set the FLASK-APP environment variable.
- Initialize the database
- Create database migration script
- Run database migration
- Start the application

```bash
$ export FLASK_APP=microblog.py
$ flask db init
$ flask db migrate
$ flask db upgrade
$ flask run
```
