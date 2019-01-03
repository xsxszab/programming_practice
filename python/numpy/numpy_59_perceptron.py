#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:03:49 2018

@author: xsxsz
"""

import numpy as np

def ReLU(x):
    return max(x,0)

def perceptron(x,y,iter):
    n=np.shape(x)[1]
    m=len(x)
    theta=np.ones(n)
    alpha=0.02
    for it in range(iter):
        l=0
        print(it)
        print('-----------')
        for k in range(m):
            a=ReLU(x[k].dot(theta.T))
            if (a)*y[k]<0:
                l=1
                theta+=alpha*(y[k]-a)*x[k]
        if l==0:
            break
    return theta

N=3
a=range(2**N)
x=[bin(i)[2:].zfill(N) for i in a]
data=np.array([[int(i) for i in j ]for j in x])
y=np.array([i[0]*i[2] for i in data])
y[y==0]=-1
theta = perceptron(data, np.array(y), 100)
for i,j in zip(data,np.array(y)):
    print(ReLU(i.dot(theta.T))* j>=0)