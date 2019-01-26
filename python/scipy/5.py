#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:50:50 2019

@author: xsxsz
"""

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

def func(x,p):
    k,theta=p[0],p[1]
    return np.sin(2*np.pi*k*x+theta)

def residuals(p, y, x):
    return y - func(x, p)

x = np.linspace(0, -2*np.pi, 100)
k, theta =0.34, np.pi/6
real=func(x,[k,theta])
test=real+0.2*np.random.randn(len(x))
p0=[0.4,0.2,0]
plsq=leastsq(residuals,p0,args=(test,x))
plt.plot(x,real,color="g")
plt.plot(x,test,color="b")
plt.plot(x,func(x,plsq[0]),color="r")