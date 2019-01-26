#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:17:55 2019

@author: xsxsz
"""

import numpy as np
from scipy.misc import derivative

def func1(x):
    return x**5

def func2(x):
    return 5*(x**4)

for x in range(1,4):
    print(func2(x))
print('----------------')
for x in range(1,4):
    print(derivative(func1,x,dx=1e-8))
print('----------------')
for x in range(1,4):
    print(derivative(func1,x,dx=1e-8,n=2))