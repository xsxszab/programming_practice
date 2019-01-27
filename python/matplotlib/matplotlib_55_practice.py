#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:49:07 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure(0)
ax=fig.add_subplot(111,projection='3d')
u=np.linspace(0, 2*np.pi, 100)
v=np.linspace(0, np.pi, 100)
x=10*np.outer(np.cos(u), np.sin(v))
y=10*np.outer(np.sin(u), np.sin(v))
z=10*np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x,y,z,color="g")