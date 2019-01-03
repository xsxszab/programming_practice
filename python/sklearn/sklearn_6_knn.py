#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 22:02:34 2018

@author: xsxsz
"""

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris=datasets.load_iris()
x=iris.data
y=iris.target
print(x.shape)
print('--------')
rand=np.random.permutation(len(x))
x_train=x[rand[:-10]]
y_train=y[rand[:-10]]
x_test=x[rand[-10:]]
y_test=y[rand[-10:]]
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
predict=knn.predict(x_test)
print(predict)
print('--------')
score=knn.score(x_test,y_test,sample_weight=None)
print(score)
print('--------')
