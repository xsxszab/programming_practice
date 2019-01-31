#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:04:05 2019

@author: xsxsz
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition import PCA

x,y=make_blobs(n_samples=10000,n_features=3,\
               centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]],\
               cluster_std=[0.2, 0.1, 0.2, 0.2],random_state=9)
fig=plt.figure()
ax=Axes3D(fig,rect=[0,0,1,1],elev=30,azim=30)
plt.scatter(x[:,0],x[:,1],x[:,2],marker='o',color='g')
pca1=PCA(n_components=3)
pca1.fit(x)
print(pca1.explained_variance_)
print('------------')
print(pca1.explained_variance_ratio_)
print('------------')
pca2=PCA(n_components=2)
pca2.fit(x)
print(pca2.explained_variance_)
print('------------')
print(pca2.explained_variance_ratio_)
print('------------')
x_new=pca2.transform(x)
plt.figure()
plt.scatter(x_new[:,0],x_new[:,1],marker='o',color='b',alpha=0.6)
pca3=PCA(n_components=0.99)
pca3.fit(x)
print(pca3.explained_variance_)
print('------------')
print(pca3.explained_variance_ratio_)
print('------------')
print(pca3.n_components_)
print('------------')
