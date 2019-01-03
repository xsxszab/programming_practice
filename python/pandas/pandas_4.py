# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:29:04 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
list=np.array([2,3,4,3,5,67,9])
index=['a','s','f','v','t','h','o']
a=pd.Series(list)
print(a)
print('-------')
a=pd.Series(list,index=index)
print(a)
print('-------')
print(a.index)
print('-------')
print(a.values)
print('-------')
print(a[0])
print('-------')
print(a['o'])
print('-------')
print('a' in a)
print('-------')
print('2' in a)
print('-------')
print(2 in a)
print('-------')
