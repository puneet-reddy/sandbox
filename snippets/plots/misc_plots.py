#!/usr/bin/env python

from matplotlib.pyplot import (
    figure, plot, subplot, barh, bar, boxplot, scatter, show, grid, hist
)


x = [1, 2, 3, 4]
y = [5, 4, 3, 2]

figure('Miscellaneous plots')

# Line plot
subplot(231)
plot(x, y)

# Bar graph
subplot(232)
bar(x, y)

# Horizontal bar graph
subplot(233)
barh(x, y)

# Stacked bar (2 bar plots on the same subplot)
subplot(234)
bar(x, y)
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')

# Box plot
subplot(235)
boxplot(x)

# Scatter graph
subplot(236)
scatter(x, y)

dataset = [113, 115, 119, 121, 124,
           124, 125, 126, 126, 126,
           127, 127, 128, 129, 130,
           130, 131, 132, 133, 136]

figure('Using 1D dataset')
subplot(121)
boxplot(dataset, vert=False)
subplot(122)
hist(dataset)

show()
