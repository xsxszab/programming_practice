#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:03:22 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

samples=25
x=np.random.normal(5,1,samples)
y=np.random.normal(3,0.5,samples)
fig=plt.figure(figsize=(6,8))
ax=fig.add_subplot(211,projection='3d')
hist,xedges,yedges=np.histogram2d(x,y,bins=10)
elements=(len(xedges)-1)*(len(yedges)-1)
xpos,ypos=np.meshgrid(xedges[:-1]+0.25,yedges[:-1]+0.25)
xpos=xpos.flatten()
ypos=ypos.flatten()
zpos=np.zeros(elements)
dx=0.1*np.ones_like(zpos)
dy=0.1*np.ones_like(zpos)
dz=hist.flatten()
ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='b',alpha=0.4)
ax=fig.add_subplot(212)
ax.scatter(x,y,color='g',label='data')
ax.legend()
ax.grid()