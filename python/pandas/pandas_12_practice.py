#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:31:46 2018

@author: xsxsz
"""

import numpy as np
import pandas as pd

df1 =pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 =pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

print(df1)
print('------------')
print(df2)
print('------------')
print(pd.merge(df1,df2))
print('------------')
print(pd.merge(df1,df2,on='key'))
print('------------')
print(pd.merge(df1,df2,how='left'))
print('------------')
print(pd.merge(df1,df2,how='right'))
print('------------')
