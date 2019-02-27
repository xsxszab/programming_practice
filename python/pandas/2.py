# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:01:59 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

data = np.random.randn(1000)
cats = pd.qcut(data,4)
print(cats)
print('-------------------------')
print(pd.value_counts(cats))
print('-------------------------')

df = pd.DataFrame(np.arange(20).reshape(5,4))
sampler = np.random.permutation(5)
print(df.take(sampler[:4]))
print('-------------------------')
