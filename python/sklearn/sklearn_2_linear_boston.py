#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:04:29 2018

@author: xsxsz
"""

from sklearn import datasets
from sklearn.linear_model import LinearRegression

data=datasets.load_boston()
x=data.data
y=data.target
print(x.shape)
print('-------')

model=LinearRegression()
model.fit(x,y)

print(model.coef_)
print('-------')
print(model.intercept_)
print('-------')
print(model.predict(x[:4,:]))
print('-------')
print(model.get_params())
print('-------')
print(model.score(x,y))
print('-------')
