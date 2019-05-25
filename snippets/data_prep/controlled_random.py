#!/usr/bin/env python

'''
Generating controlled random datasets
'''

import pylab
import random

SAMPLE_SIZE = 100

#Uses system current time with no args
random.seed()

# Completely random
real_rand_vars = []

real_rand_vars = [random.random() for val in range(SAMPLE_SIZE)]
pylab.hist(real_rand_vars, 10)

pylab.xlabel("Number range")
pylab.ylabel("Count")


# Random time series
duration = 100 #days
mean_inc = 0.2
std_inc = 1.2
x = range(duration)
y = []
start_value = 0

for i in x:
    next_delta = random.normalvariate(mean_inc, std_inc)
    start_value += next_delta
    y.append(start_value)

pylab.plot(x, y)
pylab.xlabel("Time")
pylab.ylabel("Value")
pylab.show()