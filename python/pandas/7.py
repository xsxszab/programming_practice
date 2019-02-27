# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:37:03 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

people = pd.DataFrame(np.random.randn(5,6),\
                      columns=['a','b','c','d','e','f'],\
                      index=['Joe','Steve','Wes','Jim','Travis'])
key = ['one','two','one','two','one']
print(people)
print('-------------')
print(people.groupby(key).transform(np.mean))
print('-------------')
