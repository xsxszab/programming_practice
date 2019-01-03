#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:43:21 2018

@author: xsxsz
"""

import numpy as np
from sklearn import linear_model
clf=linear_model.LinearRegression()
x=np.array([[1,2,5],[2,3.5,3.2],[4,7,1]])
y=[0,1,2]
clf.fit(x,y)
print(clf.coef_)
print('-------')
print(clf.intercept_)
print('-------')
