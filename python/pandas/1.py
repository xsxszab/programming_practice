# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:57:07 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
labels=['Youth','YoungAdult','MiddleAged','Senior']
cat1=pd.cut(ages,bins,labels=labels,right=False)
print(cat1)
print('-------------')

cat2=pd.cut(np.random.rand(10),4,precision=2)
print(cat2)
print('-------------')
