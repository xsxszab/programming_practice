#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:33:17 2019

@author: xsxsz
"""

import numpy as np

arr=np.array([[0,1,2],[3,4,5],[5,6,7]])
print(arr)
print('---------------')
print(arr.cumsum())
print('---------------')
print(arr.cumsum(0))
print('---------------')
print(arr.cumsum(1))
print('---------------')
print(arr.cumprod())
print('---------------')
print(arr.cumprod(0))
print('---------------')
print(arr.cumprod(1))
print('---------------')
