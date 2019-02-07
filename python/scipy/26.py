#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:25:03 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.random.rand(1200) * 4.0 - 2.0
y = np.random.rand(1200) * 4.0- 2.0
z = x * np.exp(-x ** 2 - y ** 2)
rf = Rbf(x, y, z,epsilon = 2)
xi, yi = np.meshgrid(np.linspace(-2.0, 2.0, 34), np.linspace(-2.0, 2.0, 34))
zi = rf(xi, yi)

plt.figure(figsize=(12,10))
ax1 = plt.subplot2grid((1,2), (0,0), projection='3d')
ax1.scatter(x,y,z,color='g')
ax2=plt.subplot2grid((1,2),(0,1),projection='3d')
ax2.scatter(xi,yi,zi,color='b')
