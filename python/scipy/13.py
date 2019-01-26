#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:58:01 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y,t):
    return -2*y*t

y0,a,b=1,0,2
t=np.arange(a,b,0.01)
y=odeint(f,y0,t)
plt.plot(t,y,color="g")