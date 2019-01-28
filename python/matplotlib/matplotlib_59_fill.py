#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:44:41 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,1000)
y1=np.sin(x)
y2=np.cos(x)
fig=plt.figure()
ax=plt.gca()
ax.plot(x,y1,color='k')
ax.plot(x,y2,color='k')
ax.fill_between(x,y1,y2,color='b',where=(y2>y1),interpolate=True)
ax.fill_between(x,y1,y2,color='g',where=(y2<y1),interpolate=True)
plt.title('$fill between$')
