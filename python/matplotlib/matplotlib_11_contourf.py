# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:56:53 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,5)
y=np.linspace(-5,5,5)
a,b=np.meshgrid(x,y)
h=[[0,0,1,2,2],[0,-2,-2,1,5],[4,2,6,8,1],[3,-3,-3,0,5],[1,-5,-2,0,3]]
plt.figure(figsize=(6,6))
plt.contourf(a,b,h,20,alpha=0.8,cmap=plt.cm.hot)
line=plt.contour(x,y,h,colors='black',linewidth=0.5)
plt.clabel(line,inline=True)
plt.xlabel('X')
plt.ylabel('Y')
