#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:51:40 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=plt.gca(projection='3d')
x,y=np.meshgrid(np.linspace(-10,10,100),np.linspace(-10,10,100))
z=x**2+(50*y**2)
ax.plot_surface(x,y,z,cmap='cool')
