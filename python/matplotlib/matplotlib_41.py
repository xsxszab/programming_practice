#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:39:50 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
fig1=plt.figure(figsize=(6,5))
ax=fig1.add_axes([1,1,1,1],polar=True)
list=np.linspace(0,100*np.pi,num=200)
ax.plot(list)

fig2=plt.figure(figsize=(6,5))
plt.subplot(111,polar=True)
theta = np.arange(0, 2*np.pi, 0.02)
plt.plot(theta,0.5*np.ones_like(theta),color='g')
