#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:15:54 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
x= np.array([0, 1, 2, 3, 4, 5, 6, 7])
y= np.array([3, 4, 3.5, 2, 1, 1.5, 1.25, 0.9])
X = np.linspace(x.min(), x.max(), 100)
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(x, y)
for n in ['linear','zero', 'slinear', 'quadratic', 'cubic',  4, 5]:
    f = interp1d(x, y, kind = n)
    ax.plot(X, f(X), label= n)
ax.legend()
ax.set_ylabel(r"$y$")
ax.set_xlabel(r"$x$")