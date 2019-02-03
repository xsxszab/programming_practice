#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:35:32 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

x=np.array([1,2,3,4])
mat=scipy.vander(x,increasing=True)
print(mat)
print('----------------')
y=np.array([1,3,5,4])
ans=np.linalg.solve(mat,y)
print(ans)
print('----------------')
plt.scatter(x,y,color='g')
def func(x):
    return ans[0]+ans[1]*x+ans[2]*x**2+ans[3]*x**3

X=np.linspace(1,4,100)
plt.plot(X,func(X),color='b')
