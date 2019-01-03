#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:02:08 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x=np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y=np.array([2,5,6.5,6.8,8,8.5,9,9.5])
plt.scatter(x,y,color='b',marker='^')
plt.grid(alpha=0.8)

poly=PolynomialFeatures(degree=3)
x_transformed=poly.fit_transform(x)
poly_linear_model=LinearRegression()
poly_linear_model.fit(x_transformed,y)

X=np.linspace(0,10,100)
X_transformed=poly.fit_transform(X.reshape(-1,1))
Y=poly_linear_model.predict(X_transformed)
plt.title('Polynominal_Regression')
plt.plot(X,Y,color='g')