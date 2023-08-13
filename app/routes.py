from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Juan'}
    posts = [
        {
            'author': {'username': 'Rick'},
            'body':'Beautyful day in Toronto!'
        },
        {
            'author': {'username': 'Susan'},
            'body':'Great Movie!'
        }
    ]
    return render_template('index.html', title='Home', user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if a user is already logged in will be redirected to the index page
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # Actual Log In
    form = LoginForm()
    if form.validate_on_submit():
        #Load the user from the db using the username
        user = User.query.filter_by(username= form.username.data).first()

        #if do not exist or the password is wrong returns a flash message and redirects to the login form
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        # Registers the user as logged In
        login_user(user, remember=form.remember_me.data)
        
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
