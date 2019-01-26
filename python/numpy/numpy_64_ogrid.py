#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:26:00 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x,y=np.ogrid[0:20:2,0:10:2]
print(x)
print('------------------------')
print(y)
print('------------------------')
x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2)
fig=plt.figure(0)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)