#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:46:32 2018

@author: xsxsz
"""

import pickle
from sklearn import svm
from sklearn import datasets
clf=svm.SVC()
iris=datasets.load_iris()
X,Y=iris.data,iris.target
print(X.shape)
print('--------')
print(Y.shape)
print('--------')
clf.fit(X,Y)
print(clf)
print('--------')

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print(clf2.predict(X[0:1]))
