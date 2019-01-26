#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:26:08 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def func(x,arg):
    return x+arg

value,err=integrate.quad(func,1,2,args=(1))
print(value)
print('------------------')
x=np.linspace(1,2,100)
y=x+1
value=integrate.trapz(y, x)
print(value)
