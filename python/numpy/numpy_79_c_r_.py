#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 20:31:36 2019

@author: xsxsz
"""

import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

result1=np.c_[arr1,arr2]
print(result1)
print('-------------')
result2=np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
print(result2)
print('-------------')
result3=np.r_[np.array([1,2,3]), 0, 0, np.array([4,5,6])]
print(result3)
print('-------------')
