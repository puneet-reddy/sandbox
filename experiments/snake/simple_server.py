#!/usr/bin/env python

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('html5_snake.html')

@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    app.run(debug=True)