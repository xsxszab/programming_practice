#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:36:59 2018

@author: xsxsz
"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier
X=np.array([[0,1],[3,4]])
Y=[1,5]
clf=DecisionTreeClassifier()
clf.fit(X,Y)
print(clf.predict([[0,0]]))
