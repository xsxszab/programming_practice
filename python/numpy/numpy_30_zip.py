#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:58:33 2018

@author: xsxsz
"""

import numpy as np
x=np.array([1,2,3,4])
y=np.array([0,9,8,7])
a=list(zip(x,y))
print(x)
print('----------')
print(y)
print('----------')
print(a)
print('----------')
b,c=zip(*zip(x,y))
print(b)
print('----------')
print(c)
print('----------')
