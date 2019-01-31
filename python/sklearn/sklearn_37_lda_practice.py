#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:24:35 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_classification
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def func(arr):
    colors=[]
    for i in arr:
        if i==0:
            colors.append('r')
        elif i==1:
            colors.append('g')
        elif i==2:
            colors.append('b')
    return colors

x,y=make_classification(n_samples=1000,n_features=3,n_redundant=0,n_classes=3,\
                        n_informative=2,n_clusters_per_class=1,class_sep=0.5,\
                        random_state=10)
fig=plt.figure()
ax=Axes3D(fig,rect=[0,0,1,1],elev=30,azim=30)
colors=func(y)
ax.scatter(x[:,0],x[:,1],x[:,2],marker='o',color=colors)
lda=LinearDiscriminantAnalysis(n_components=2)
lda.fit(x,y)
x_new=lda.transform(x)
plt.figure()
plt.scatter(x_new[:,0],x_new[:,1],color=colors,marker='o',alpha=0.6)
plt.title('LDA')
