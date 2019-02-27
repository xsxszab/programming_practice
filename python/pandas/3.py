# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:06:04 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'key1' :['a','a','b','b','a'],
    'key2':['one','two','one','two','one'],
    'data1':np.random.randn(5),
    'data2':np.random.randn(5)
})
print(df)
print('-------------')
group1 = df['data1'].groupby(df['key1'])
print(group1.mean())
print('-------------')
group2 = df['data1'].groupby(df['key2'])
print(group2.mean())
print('-------------')
