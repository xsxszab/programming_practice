#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:48:08 2019

@author: xsxsz
"""

import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
for z in [2011,2012,2013,2014]:
    xs=range(1,13)
    ys=1000*np.random.rand(12)
    color=plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
    ax.bar(xs,ys,zs=z,zdir='y',color=color,alpha=0.8)

ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))
ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))
ax.set_xlabel('Month')
ax.set_ylabel('Year')
ax.set_zlabel('value')
