#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:46:25 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x=np.linspace(0, 2*np.pi+np.pi/4, 10)
y=np.sin(x)
x_new=np.linspace(0, 2*np.pi+np.pi/4, 100)
f_linear=interpolate.interp1d(x, y)
tck=interpolate.splrep(x, y)
y_bspline=interpolate.splev(x_new, tck)
plt.scatter(x,y,color="r")
plt.plot(x_new, f_linear(x_new),color="g")
plt.plot(x_new, y_bspline,color="b")