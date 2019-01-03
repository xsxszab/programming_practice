#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:34:05 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
X = np.array([0 , 4, 10, 15, 21, 29, 36, 51, 68,100])
y = np.array([[66.7, 71.0, 76.3, 80.6, 85.7, 92.9, 99.4, 113.6, 125.1,140]])
X_T=np.ones(len(X)).astype(dtype=np.int)
X_new=np.array([X_T,X])
temp=np.matrix(np.dot(X_new,X_new.T))
ans= temp ** -1 * X_new * y.T
intercept=np.array(ans)[0][0]
coef=np.array(ans)[1][0]
lx=np.arange(0,100)
ly=coef*lx+intercept
plt.figure(figsize=(5,6))
plt.title('normal equation')
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(X,y,color='b')
plt.plot(lx,ly,color='g')
