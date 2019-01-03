#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:57:18 2018

@author: xsxsz
"""

import numpy as np
import pandas as pd
obj=pd.Series([4,np.NAN,-5,3],index=['a','b','c','d'])
print(obj)
print('------------')
print(obj.values)
print('------------')
print(obj.index)
print('------------')
print(obj['a'])
print('------------')
print(obj.isnull())
print('------------')
print(obj.notnull())
print('------------')
obj1=pd.Series([2],index=['d'])
obj+=obj1
print(obj)
print('------------')
print(obj.name)
print('------------')
obj.name='Series'
print(obj.name)
print('------------')
obj.index=['ha','haha','hahaha','hahahaha']
print(obj)
print('------------')
