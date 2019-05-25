#!/usr/bin/env python

import matplotlib.pyplot as plt


plt.figure()

plt.subplot(221)
plt.plot([1,2,3,2,3,2,2,1])

plt.subplot(222)
plt.plot([4,3,2,1],[1,2,3,4])

plt.show()