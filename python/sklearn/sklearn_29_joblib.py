#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:22:42 2018

@author: xsxsz
"""

import numpy as np
from sklearn.externals import joblib
from sklearn import svm
x=[[0,0],[1,1]]
y=[0,1]
clf=svm.SVC()
clf.fit(x,y)
joblib.dump(clf,'moduel')
