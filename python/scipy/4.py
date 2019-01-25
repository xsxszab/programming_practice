#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:33:42 2019

@author: xsxsz
"""

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def f(x):
     return x**2 + 10*np.sin(x)
x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
optimize.fmin_bfgs(f,0)