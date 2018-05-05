from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': "Travis"}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'This site sucks, get better!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'Wow dude, just wow...'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title="Sign In", form=form)