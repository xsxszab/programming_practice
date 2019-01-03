#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:33:17 2018

@author: xsxsz
"""

import numpy as np
from sklearn import datasets
from sklearn import svm
clf=svm.SVC(gamma='auto',kernel='rbf')
data_iris=datasets.load_iris()
x=data_iris.data
y=data_iris.target
print(x.shape)
print('--------------')
clf.fit(x,y)
test = np.array([[5.1,2.9,1.8,3.6]])
print(clf.predict(test))
print('--------------')
