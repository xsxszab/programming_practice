#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:46:10 2018

@author: xsxsz
"""

import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris=load_iris()
X=iris.data
Y=iris.target
clf=tree.DecisionTreeClassifier(max_depth=10)
clf.fit(X,Y)
print(clf)
print('-----------')
print(clf.predict([[1,2,3,4]]))