#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:42:36 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.datasets import make_gaussian_quantiles
X1,Y1=make_classification(n_samples=400,n_features=2
,n_redundant=0,n_clusters_per_class=1,n_classes=4)
print(Y1)
print('------------')
plt.figure(figsize=(10,6))
plt.subplot(121)
plt.scatter(X1[:,0],X1[:,1],c=Y1,s=3,marker='^')
plt.subplot(122)
X2,Y2=make_gaussian_quantiles(mean=[2,7,8],cov=10,n_samples=200,n_features=3)
print(X2)
print('------------')
print(Y2)
print('------------')
plt.scatter(X2[:,0],X2[:,1],c=Y2)