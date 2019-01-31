#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:48:36 2019

@author: xsxsz
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from io import StringIO

csv_data = 'square_feet,price\n150,6450\n200,7450\n250,8450\n300,9450\n350,11450\n400,15450\n600,18450\n'
df=pd.read_csv(StringIO(csv_data))
print(df)
print('------------')
model=linear_model.LinearRegression()
model.fit( df['square_feet'].values.reshape(-1,1), df['price'] )
coef,intercept=model.coef_,model.intercept_
print(coef)
print('------------')
print(intercept)
print('------------')
area=200
print(coef*area+intercept)
print('------------')
print(model.predict(area))
print('------------')
plt.scatter( df['square_feet'].values, df['price'] ,color='g')
plt.plot(df['square_feet'], model.predict(df['square_feet'].values.reshape(-1,1)),\
         color='r')
