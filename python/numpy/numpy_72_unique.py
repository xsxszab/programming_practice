#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:44:30 2019

@author: xsxsz
"""

import numpy as np

arr=np.array([1,2,3,4,7,8,7,43,2,2,2,3,5,6,43,2,8])
print(arr)
print('---------------')
print(np.unique(arr))
print('---------------')
print(np.in1d(arr,[1,2,3,4,5]))
print('---------------')
print(np.intersect1d([1,2,3,4,5,6],[4,5,6,7,8,9]))
print('---------------')
print(np.setdiff1d([1,2,3,4,5,6],[4,5,6,7,8,9]))
print('---------------')
print(np.setdiff1d([4,5,6,7,8,9],[1,2,3,4,5,6]))
print('---------------')
print(np.union1d([1,2,3],[4,5,6]))
print('---------------')
print(np.setxor1d([1,2,3,4,5,6],[4,5,6,7,8,9]))
print('---------------')
