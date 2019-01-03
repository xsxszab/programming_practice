# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:22:20 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,100)
y=np.linspace(-1,1,100)
x1,y1=np.meshgrid(x,y)
z=np.sqrt(x1**2+y1**2)
fig=plt.figure()
ax=fig.add_subplot(221)
ax1=fig.add_subplot(222)
ax2=fig.add_subplot(223)
ax3=fig.add_subplot(224)
ax.imshow(z)
ax1.imshow(z,cmap=plt.cm.cool)
ax2.imshow(z,cmap=plt.cm.hot)
ax3.imshow(z,cmap=plt.cm.gist_rainbow)
