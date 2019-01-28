#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:55:19 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

def aver(interval,window_size):
    window=np.ones(int(window_size))/float(window_size)
    return np.convolve(interval,window,'same')

time=np.linspace(-4,4,100)
y=np.sin(time)+np.random.randn(len(time))*0.1

plt.scatter(time,y,color='g')
y_aver=aver(y,10)
plt.plot(time,y_aver,color='b',linewidth=2)
