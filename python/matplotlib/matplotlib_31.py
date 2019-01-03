# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:58:06 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x,y,c='r')
ax1.set_title('area1')
left1, bottom1, width1, height1 = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left1, bottom1, width1, height1])
ax2.plot(x,y,c='b')
ax2.set_title('area2')
