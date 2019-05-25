#!/usr/bin/env python

'''
Visualizing different distributions
'''

import random
import matplotlib
import matplotlib.pyplot as plt

SAMPLE_SIZE = 1000
buckets = 100

plt.figure()
matplotlib.rcParams.update({'font.size': 7})
plt.subplot(621)
plt.xlabel('random.random')

data = [random.random() for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(622)
plt.xlabel('random.uniform')
a = 1
b = SAMPLE_SIZE
data = [random.uniform(a, b) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(623)
plt.xlabel('random.triangular')
low = 1
high = SAMPLE_SIZE
data = [random.triangular(low, high) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(624)
plt.xlabel('random.betavariate')
alpha = 1
beta = 10
data = [random.betavariate(alpha, beta) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(625)
plt.xlabel('random.expovariate')
lamb = 1.0/((SAMPLE_SIZE + 1) / 2.)
data = [random.expovariate(lamb) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(626)
plt.xlabel('random.gammavariate')
alpha = 1
beta = 10
data = [random.gammavariate(alpha, beta) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(627)
plt.xlabel('random.logvariate')
mu = 1
sigma = 0.5
data = [random.lognormvariate(mu, sigma) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(628)
plt.xlabel('random.normalvariate')
mu = 1
sigma = 0.5
data = [random.normalvariate(mu, sigma) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.subplot(629)
plt.xlabel('random.paretovariate')
alpha = 1
data = [random.paretovariate(alpha) for _ in range(1, SAMPLE_SIZE)]
plt.hist(data, buckets)

plt.tight_layout()
plt.show()