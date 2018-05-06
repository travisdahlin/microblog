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
$ sudo pip install flask
```
- Install flask-wtf
```bash
$ sudo pip install flask-wtf
```
 - Install flask-sqlalchemy
 ```bash
 $ sudo pip install flask-sqlalchemy
 ```
 - Install flask-migrate
 ```bash
 $ sudo pip install flask-migrate
 ```
- Set the FLASK-APP environment varialb.
```bash
$ export FLASK_APP=microblog.py
```
- Start the application
```bash
$ flask run
```