#!/usr/bin/env python

from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/')
def home():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)