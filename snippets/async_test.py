#!/usr/bin/env python

import time
import threading
from flask import Flask
from collections import deque

app = Flask(__name__)

messages = deque()


def consume(msg=None):
    time.sleep(5)
    print(msg)


@app.route('/')
def home():
    msg = 'Hello from the home function.'
    threading.Thread(target=consume, args=(msg,)).start()
    messages.append(msg)
    return "Just a dummy home page."

if __name__ == '__main__':
    app.run(debug=True)