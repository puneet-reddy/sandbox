
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    data = {'username': 'Puneet'}
    posts = [
        {
            'author': {'username': 'Johen'},
            'body': "My name is John not Johen!!!"
        },
        {
            'author': {'username': 'Anon'},
            'body': "I'm not anonymous, my name IS Anon"
        }
    ]
    return render_template('index.html', title='Home', data=data, posts=posts)
