# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:39:37 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([2,4,6,9,16,24,6,2,4,0])
plt.plot(x,y,'r',lw=3)
plt.plot(x-1,y+1,'g',lw=5)
plt.bar(x,y,0.6,alpha=0.9,color='b')