#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:05:39 2018

@author: xsxsz
"""

import numpy as np
from sklearn.model_selection import train_test_split
X=np.linspace(10,50,40,dtype=int).reshape(5,8)
print(X)
print('----------')
y=list(range(5))
print(y)
print('----------')
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=42)
print(X_train)
print('----------')
print(X_test)
print('----------')
print(y_train)
print('----------')
print(y_test)   
print('----------')
