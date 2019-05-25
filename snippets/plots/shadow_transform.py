#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms


def setup(layout=None):
    assert layout is not None

    fig = plt.figure()
    ax = fig.add_subplot(layout)
    return fig, ax


def get_signal():
    t = np.arange(0., 1.5, 0.01)
    s = np.sin(5 * np.pi * t)
    return t, s


def plot_signal(t, s):
    line, = axes.plot(t, s, color='#0D34C6')
    return line


def make_shadow(fig, axes, line, t, s):
    # How much to move the shadow
    delta_x = 3/100.
    delta_y = -7/100.

    offset = transforms.ScaledTranslation(delta_x, delta_y, fig.dpi_scale_trans)
    offset_transform = axes.transData + offset
    axes.plot(t, s, color='00050', transform=offset_transform,
              zorder=0.5 * line.get_zorder())


if __name__ == '__main__':
    fig, axes = setup(111)
    t, s = get_signal()
    line = plot_signal(t, s)
    make_shadow(fig, axes, line, t, s)

    axes.set_title('Shadow effect using an offset transform')
    plt.show()
