#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:34:40 2019

@author: xsxsz
"""

import numpy as np

a1 = np.concatenate(([3], [8] * 4, np.arange(1, 6)))
print(a1)
print('------------------------')
x1 = np.array([[1,2,3],[4,5,6]])
x2 = np.array([[11,12,13],[14,15,16]])
a2 = np.concatenate((x1,x2), axis = 0)
print(a2)
print('------------------------')
a3 = np.concatenate((x1,x2), axis = 1)
print(a3)
print('------------------------')
a4 = np.concatenate((x1,x2), axis = None)
print(a4)
print('------------------------')
a5 = np.concatenate((x1,x2))
print(a5)
a4 = np.concatenate((x1,x2), axis = None)