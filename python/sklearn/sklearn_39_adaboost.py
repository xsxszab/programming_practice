#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 20:11:39 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_gaussian_quantiles
from sklearn.tree import DecisionTreeClassifier

depth=2

x1,y1=make_gaussian_quantiles(cov=2., n_samples=200, n_features=2,\
                              n_classes=2, shuffle=True, random_state=1)
x2,y2=make_gaussian_quantiles(mean=(3,3), cov=1.5, n_samples=300,\
                              n_features=2, n_classes=2, shuffle=True, random_state=1)
x=np.vstack((x1,x2))
y=np.hstack((y1,1-y2))
classifier=DecisionTreeClassifier(max_depth=depth)
clf=AdaBoostClassifier(base_estimator=classifier,\
                       algorithm='SAMME',n_estimators=300,learning_rate=0.8)
clf.fit(x,y)
x1_min=x[:,0].min()
x1_max=x[:,0].max()
x2_min=x[:,1].min()
x2_max=x[:,1].max()
x1_,x2_=np.meshgrid(np.arange(x1_min,x1_max,0.02),np.arange(x2_min,x2_max,0.02))
y_=clf.predict(np.c_[x1_.ravel(),x2_.ravel()])
y_=y_.reshape(x1_.shape)
plt.contourf(x1_,x2_,y_,cmap=plt.cm.Paired)
plt.scatter(x[:,0],x[:,1],c=y)
plt.title('$Adaboost$')
