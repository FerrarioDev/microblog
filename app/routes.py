from app import app
from flask import render_template

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
