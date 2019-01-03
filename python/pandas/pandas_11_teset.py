#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:17:59 2018

@author: xsxsz
"""

import numpy as np
import pandas as pd
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
print(obj)
print('-------------')
print(obj.reindex(['d','a','b','c']))
print('-------------')
print(obj.reindex(['d','a','b','c','e'],fill_value=0))
print('-------------')
obj1=pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj1)
print('-------------')
print(obj1.reindex(range(6),method='ffill'))
print('-------------')
obj2=pd.Series([1,2,3,np.NAN])
print(obj2)
print('-------------')
print(obj2.dropna())
print('-------------')
