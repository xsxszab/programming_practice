#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:52:29 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition import PCA

X, y = make_blobs(n_samples=10000,n_features=3,centers=[[3,3,3],[0,0,0],[1,1,1],[2,2,2]], 
cluster_std=[0.2,0.1,0.2,0.2],random_state=9)
fig=plt.figure(figsize=(6,5))
ax = Axes3D(fig,rect=[0,0,1,1],elev=35,azim=30)
ax.scatter(X[:,0],X[:,1],X[:,2],marker='o',color='b')
pca=PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_)
print('------------')
print(pca.explained_variance_ratio_)
print('------------')
x=pca.transform(X)
print(x)
print('------------')
plt.figure()
plt.scatter(x[:,0],x[:,1],c='g',marker='o')
