#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:17:09 2019

@author: xsxsz
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

def func(x):
    return x**2+x*2

x=np.linspace(-10,10,1000)
y=func(x)
plt.plot(x,y,"b")
x=10
ans=scipy.optimize.fmin(func,x)
plt.scatter(ans,func(ans),color='g')