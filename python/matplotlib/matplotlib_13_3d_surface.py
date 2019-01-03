# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:31:16 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
a=np.arange(-4,4,0.1)
b=np.arange(-1,4,0.1)
x,y=np.meshgrid(a,b)
fig=plt.figure()
ax=Axes3D(fig)
z=x**2+y**2
plt.title('3d')
ax.set_xlabel('X',color='r')
ax.set_ylabel('Y',color='g')
ax.set_zlabel('Z',color='b')
ax.plot_surface(x,y,z,cstride=2,rstride=2,cmap=plt.cm.cool,alpha=0.95)
#ax.plot_surface(x,y,z,cstride=2,rstride=2,cmap=plt.cm.cool_r,alpha=0.95)
ax.scatter(x+5,y,z)
ax.view_init(elev=30,azim=45)
