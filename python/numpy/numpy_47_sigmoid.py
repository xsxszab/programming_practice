#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:44:18 2018

@author: xsxsz
"""

import numpy as np

mat=[[-10,-8,-7,-6,-5],
     [-4,-3,-2,-1,0],
     [0,1,2,3,4],
     [5,6,7,8,10]]
print(mat)
print('---------')

def sigmoid(x):
    return 1/(1+np.exp(-x))

result=np.zeros([4,5])
for i,line in enumerate(mat):
    result[i]=list(map(sigmoid,line))

print(result)
print('---------')
