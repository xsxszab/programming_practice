#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:53:02 2018

@author: xsxsz
"""

from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
clf = svm.SVC()
iris = datasets.load_iris()
X, Y = iris.data, iris.target
clf.fit(X, Y)
joblib.dump(clf,'classifier.pkl')

clf1=joblib.load('classifier.pkl')
print(clf1.predict(X[0:1]))
