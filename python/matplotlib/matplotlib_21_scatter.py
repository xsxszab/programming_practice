#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:12:23 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,5,6,9,12,18])
plt.figure()
y=x*2
size=x**2
color=np.random.rand(7)
#color=x**2
plt.scatter(x,y,s=size,marker='^',c=color,linewidths=1,edgecolors='g')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter')
