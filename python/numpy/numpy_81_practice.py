#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:24:57 2019

@author: xsxsz
"""

import numpy as np

def comparision(x):
    n=len(x)
    mat=np.eye(n)
    for i in range(n):
        for j in range(n):
            if i!=j:
                mat[i,j]=x[i]/x[j]
    return mat

def isconsist(mat):
    n=np.shape(mat)[0]
    a,b=np.linalg.eig(mat)
    l=a[0].real
    CI=(l-n)/(n-1)
    if CI<=0.1:
        return 'true'
    else:
        return 'false'
    
x=[1,3,5,7]
mat=comparision(x)
print(mat)
print('------------')
print(isconsist(mat))
print('------------')
