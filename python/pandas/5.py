# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:17:13 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

columns = pd.MultiIndex.from_arrays([['US','US','US','JP','JP'],\
                                     [1,3,2,4,5]],names=['city','tenor'])
hier_df = pd.DataFrame(np.random.randn(4,5),columns=columns)
print(columns)
print('---------------')
print(hier_df)
print('---------------')
print(hier_df.groupby(level='city',axis=1).count())
print('---------------')
