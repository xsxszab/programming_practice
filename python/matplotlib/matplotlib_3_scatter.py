# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:06:31 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
n=1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
color=np.arctan2(y,x)
plt.scatter(x,y,s=20,c=color,alpha=0.5)
plt.ylim(-1,1)
plt.xlim(-1,1)
