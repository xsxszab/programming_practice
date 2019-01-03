# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:44:47 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
for i in range(15):
    dateOne=np.zeros([2])
    dateOne[0]=i
    dateOne[1]=i
    y=np.zeros([2])
    y[0]=10
    y[1]=20
    plt.plot(dateOne,y,'r',lw=4)