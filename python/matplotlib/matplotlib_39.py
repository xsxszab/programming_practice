#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:34:22 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
x=np.linspace(-10,10)
y=np.linspace(-10,10)
X,Y=np.meshgrid(x,y)
Z1=Y*X*X
Z2=X*X+Y*Y
fig1=plt.figure(1)
ax1=Axes3D(fig1)
ax1.plot_surface(X,Y,Z1,cmap='gist_earth')
ax1.contour(X,Y,Z1,offset=-1000)
fig2=plt.figure(2)
ax2=Axes3D(fig2)
ax2.plot_surface(X,Y,Z2,cmap='gist_earth')
ax2.contour(X,Y,Z2,offset=0)    