#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:31:47 2019

@author: xsxsz
"""

import numpy as np
a1=np.array([1,2,3])
b1=np.array([1,2,4])
x1=np.vstack((a1,b1))

print(np.cov(a1,b1))
print('--------------')
print(np.cov(x1))
print('--------------')
print(np.corrcoef(a1,b1))
print('--------------')

a2=np.array([1,2,3])
b2=np.array([1,2,3])
x2=np.vstack((a2,b2))

print(np.cov(a2,b2))
print('--------------')
print(np.cov(x2))
print('--------------')
print(np.corrcoef(a2,b2))
print('--------------')
