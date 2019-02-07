#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:19:57 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

def func(x):
    return x**2 + 30*np.sin(x)



x=np.linspace(-10,10,20)
y=func(x)

plt.title('$Rbf$')
plt.grid()

plt.scatter(x,y,color='g')

rf=Rbf(x,y)
x1=np.linspace(-10,10,100)
y1=rf(x1)

plt.plot(x1,y1,color='b')
