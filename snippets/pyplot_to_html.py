#!/usr/bin/env python

'''
A very simple example on how to convert a matplotlib.pyplot image into
a base64 encoded string and use it in html.

Optionally, this could be converted to an API which just returns the img string
and we could build the actual img tag on the front end. (Better separation
of concerns)
'''

import base64
import matplotlib
import numpy as np
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from io import BytesIO
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    d = get_plot()
    return '''<img src="data:image/png;base64,%s" />''' %(d.decode('utf-8'))

def get_plot():
    img = BytesIO()
    x = np.linspace(0, 10)
    y = np.sin(x)
    plt.plot(x, y)
    plt.savefig(img, format='png')
    return base64.encodestring(img.getvalue())

if __name__ == '__main__':
    app.run(debug=True)