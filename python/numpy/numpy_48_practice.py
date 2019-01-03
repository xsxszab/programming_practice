#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:46:01 2018

@author: xsxsz
"""

import numpy as np

def integrate(func,a,b):
    area=0.0
    step=0.01
    for i in np.arange(a,b,step):
        area+=(func(i)+func(i+step))*step/2
    return area

print(integrate(np.exp,1,4))
print('---------')
print(np.exp(4)-np.exp(1))
print('---------')
