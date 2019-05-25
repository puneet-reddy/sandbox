#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def is_outlier(points, threshold=3.5):
    """
    This returns 'True' if the points are outliers and 'False' otherwise
    """
    #Transform into vector
    if len(points.shape) == 1:
        points = points[:,None]
    
    median = np.median(points, axis=0)

    #Compute diff sums along the axis
    diff = np.sum((points-median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    #Compute modified z-score
    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > threshold

# Generate some test data with outliers
test = np.random.random(1000)
buckets = 50
test = np.r_[test, -100, -50, 50, 100]

filtered = test[~is_outlier(test)]

#Plot the raw data (with outliers)
plt.figure()
plt.subplot(211)
plt.hist(test, buckets)
plt.xlabel('Raw Data')

#Plot the cleaned data (outliers removed)
plt.subplot(212)
plt.hist(filtered, buckets)
plt.xlabel('Cleaned Data')

plt.show()