#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:06:02 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron
x,y = make_classification(n_samples=1000, n_features=2,n_redundant=0,n_informative=1,n_clusters_per_class=1)
x_train,x_test,y_train,y_test=train_test_split(x,y)
positive_x1 = [x[i,0] for i in range(1000) if y[i] == 1]
positive_x2 = [x[i,1] for i in range(1000) if y[i] == 1]
negetive_x1 = [x[i,0] for i in range(1000) if y[i] == 0]
negetive_x2 = [x[i,1] for i in range(1000) if y[i] == 0]
clf=Perceptron(fit_intercept=False,n_iter=30,shuffle=False)
clf.fit(x_train,y_train)
print('-------------')
print(clf.coef_)
print('-------------')
ans=clf.score(x_test,y_test)
print(ans)
print('-------------')
plt.figure(figsize=(6,5))
plt.scatter(positive_x1,positive_x2,color='g')
plt.scatter(negetive_x1,negetive_x2,color='r')
xline=np.linspace(-5,5)
yline=xline*(-clf.coef_[0][0] / clf.coef_[0][1]) - clf.intercept_
plt.plot(xline,yline,color='b')
