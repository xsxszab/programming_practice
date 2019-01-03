#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:48:56 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
clf=GaussianNB()
clf.fit(X,Y)
plt.xkcd()
print(clf.predict([[-0.6,7]]))
print(clf.predict_proba([[-0.6,7]]))
print('-----------------')
print(clf.predict([[1,0]]))
print(clf.predict_proba([[1,0]]))
plt.figure(figsize=(6,5))
plt.scatter(X[:,0],X[:,1],color='b')
plt.scatter(-0.6,7,color='g')
plt.scatter(1,0,color='y')
