#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:18:37 2018

@author: xsxsz
"""

from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

linear_model=linear_model.LinearRegression()
boston=datasets.load_boston()
target=boston.target
predicted=cross_val_predict(linear_model,boston.data,target,cv=2)

plt.figure(figsize=(6,5))
plt.scatter(target,predicted,color='g',edgecolors=(0,0,0))
plt.plot([target.min(), target.max()], [target.min(), target.max()], 'k--', lw=4)