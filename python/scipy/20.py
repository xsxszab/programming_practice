#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:46:38 2019

@author: xsxsz
"""

import numpy as np
import scipy.linalg as linalg

a=np.mat(np.ones([3,3]))
b=np.mat(np.ones([4,3]))
c=np.mat(np.ones([3,4]))
d=linalg.block_diag(a,b,c)
print(d)
print('----------')
e=linalg.pascal(6)
print(e)
print('----------')
f_value=np.array([0.3, 0.1, 0.4, 0.2])
s_value=np.array([0.2, 0.8, 0.7])
f=linalg.leslie(f_value,s_value)
print(f)
print('----------')
