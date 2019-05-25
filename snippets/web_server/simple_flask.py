#!/usr/bin/env python

from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_world():
    return Response(
        'Hello world from Flask via a WSGI written in python!\n',
        mimetype='text/plain'
    )

wsgi_app = app.wsgi_app