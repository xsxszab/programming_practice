#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:47:12 2018

@author: xsxsz
"""

import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import LeaveOneOut
x=[1,2,3,4]
kf=KFold(n_splits=3)
for train,test in kf.split(x):
    print(train)
    print('--------')
    print(test)
    print('--------')

print('---------------------')
L=LeaveOneOut()
for train,test in L.split(x):
    print(train)
    print('--------')
    print(test)
    print('--------')