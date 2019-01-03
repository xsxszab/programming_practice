#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:43:48 2018

@author: xsxsz
"""

import numpy as np
import pandas as pd
df=pd.DataFrame((np.linspace(0,200,20).reshape(4,5)+np.random.randn(4,5)*20).astype('int'),index=list('abcd'),columns=list('12345'))
print(df)
print('---------')
print(df.values)
print('---------')
print(df.iloc[2])
print('---------')
print(df.shape)
print('---------')
print(df.head(0))
print('---------')
print(df.head(1))
print('---------')
print(df.tail())
print('---------')
print(df.tail(1))
print('---------')
print(df.index)
print('---------')
print(df.columns)
print('---------')
print(df.describe)
print('---------')
print(df.describe())
print('---------')
print(df)
print('---------')
df1=df.sort_index(axis=0,ascending=False)
print(df1)
print('---------')
print(df[1:3])
print('---------')
print(df.loc['a','1'])
print('---------')
print(df.iloc[0,1])
print('---------')
print(df)
print('---------')
df['1']=0
print(df)
df['a']=12
print(df)
print('---------')
