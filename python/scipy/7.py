#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:32:58 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [5*x1+3, 4*x0*x0-2*np.sin(x1*x2), x1*x2-1.5]

ans=fsolve(f,[1,1,1])
print(ans)
print('-------------------')
print(f(ans))
print('-------------------')
