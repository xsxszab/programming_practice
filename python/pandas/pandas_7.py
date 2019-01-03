#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:49:34 2018

@author: xsxsz
"""

import numpy as np
import pandas as pd
df=pd.DataFrame([[1,2,3],[np.nan,np.nan,2],[np.nan,np.nan,np.nan],[8,8,np.nan]],index=['A','B','C','D'])
print(df)
print('--------')
df1=df.fillna(10)
print(df1)
print('--------')
df2=df.fillna({0:10,1:20,2:30})
print(df2)
print('--------')
df3=pd.DataFrame({'A':[1,1,2,2],'B':['a','a','b','b']})
print(df3)
print('--------')
df4=df3.drop_duplicates(subset=None,keep='last',inplace=False)
print(df4)
print('--------')
df5=df3.drop('A',axis=1)
print(df5)
print('--------')
