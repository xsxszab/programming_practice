#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:26:29 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

figsize=7
colormap=lambda r: cm.Set2(r/20.0)
N=18

fig=plt.figure(figsize=(figsize,figsize))
ax=fig.add_axes([0.2,0.2,0.7,0.7],polar=True)
#ax.set_theta_direction(-1)
theta=np.arange(0.0, 2*np.pi, 2*np.pi/N)
radii=20*np.random.rand(N)
width=np.pi/4*np.random.rand(N)
bars=ax.bar(theta,radii,width=width,bottom=0.0)
for r,bar in zip(radii,bars):
    bar.set_facecolor(colormap(r))
    bar.set_alpha(0.6)

plt.title('polar')
