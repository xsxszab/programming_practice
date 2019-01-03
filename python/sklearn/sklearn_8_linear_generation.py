#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:11:56 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

plt.figure(figsize=(10,8),facecolor='#1C86EE')
model=LinearRegression()

ax1=plt.subplot(221)
X_1,y_1,coef=make_regression(n_samples=200,n_features=1,noise=0,coef=True)
plt.scatter(X_1,y_1,alpha=0.8,c='g')
model.fit(X_1,y_1)
plt.plot(X_1,X_1*model.coef_,c='k')

ax2=plt.subplot(222)
X_2,y_2,coef=make_regression(n_samples=200,n_features=1,noise=10,coef=True)
plt.scatter(X_2,y_2,alpha=0.8,c='b')
model.fit(X_2,y_2)
plt.plot(X_2,X_2*model.coef_,c='k')

ax3=plt.subplot(223)
X_3,y_3,coef=make_regression(n_samples=200,n_features=1,noise=30,coef=True)
plt.scatter(X_3,y_3,alpha=0.8,c='y')
model.fit(X_3,y_3)
plt.plot(X_3,X_3*model.coef_,c='k')

ax4=plt.subplot(224)
X_4,y_4,coef=make_regression(n_samples=1000,n_features=1,noise=50,coef=True)
plt.scatter(X_4,y_4,alpha=0.8,c='r')
model.fit(X_4,y_4)
plt.plot(X_4,X_4*model.coef_,c='k')
