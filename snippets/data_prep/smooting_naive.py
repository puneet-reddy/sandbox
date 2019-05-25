#!/usr/bin/env python

'''
Naive smoothing by averaging over a moving window
'''

import pylab
import numpy as np

def moving_average(interval, window_size):
    '''
    Compute convoluted window for given size
    '''
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')

t = np.linspace(-4, 4, 100)
y = np.sin(t) + pylab.randn(len(t))*0.1

pylab.plot(t, y, "k.")

y_av = moving_average(y, 10)
pylab.plot(t, y_av, "r")

pylab.xlabel("Time")
pylab.ylabel("Value")
pylab.grid(True)
pylab.show()