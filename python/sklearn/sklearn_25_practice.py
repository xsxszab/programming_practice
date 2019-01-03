#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:22:59 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
load=load_wine()
x=load.data
y=load.target
print(load_wine.__doc__)
print('---------')
print(x.shape)
print('---------')
print(y.shape)
print('---------')
plt.figure(figsize=(12,10))
tick=np.linspace(1,179,178,dtype='int')
color=[]
for i in range(len(y)):
    if y[i]==0:
        color.append('r')
        continue
    if y[i]==1:
        color.append('g')
        continue
    if y[i]==2:
        color.append('b')
plt.subplot(221)
plt.scatter(tick,x[:,0],c=color)
plt.subplot(222)
plt.scatter(tick,x[:,1],c=color)
plt.subplot(223)
plt.scatter(tick,x[:,2],c=color)
plt.subplot(224)
plt.scatter(tick,x[:,3],c=color)