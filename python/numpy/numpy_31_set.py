#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:50:35 2018

@author: xsxsz
"""

import numpy as np
set1=np.array([1,3,5,7,9,6,4,4,9,10,6,0])
set2=np.array([1,3,5,7,89,98,6,4,67,8,5])
print(np.unique(set1))
print('------------')
print(np.intersect1d(set1,set2))
print('------------')
print(np.union1d(set1,set2))
print('------------')
print(np.in1d(set1,set2))
print('------------')
print(np.in1d(set2,set1))
print('------------')
print(np.setdiff1d(set1,set2))
print('------------')
print(np.setdiff1d(set2,set1))
print('------------')
print(np.setxor1d(set1,set2))
print('------------')
print(np.setxor1d(set2,set1))
print('------------')
