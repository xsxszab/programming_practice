# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:22:45 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'key1' :['a','a','b','b','a'],
    'data1':np.random.randn(5),
    'data2':np.random.randn(5)
})
print(df)
print('----------------')

def func(arr):
    return arr.max()

group = df.groupby('key1')
print(group.agg(func))
print('----------------')
