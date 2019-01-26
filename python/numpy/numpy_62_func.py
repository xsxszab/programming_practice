#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:11:05 2019

@author: xsxsz
"""

import numpy as np

def func1(i):
    return i%4+1

print(np.fromfunction(func1,(10,)))
print('-------------------')
def func2(i,j):
    return i*j

print(np.fromfunction(func2,(9,9)))
print('-------------------')

