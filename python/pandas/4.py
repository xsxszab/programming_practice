# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:15:07 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

people = pd.DataFrame(np.random.randn(5,5),\
                      columns=['a','b','c','d','e'],\
                      index=['Joe','Steve','Wes','Jim','Travis'])
mapping = {'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}
print(people)
print('--------------')
print(people.groupby(mapping,axis=1).sum())
print('--------------')
print(people.groupby(len).sum())
print('--------------')
