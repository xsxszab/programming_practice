# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:01:51 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
s=pd.Series([1,2,np.nan,7])
print s
print'-------------'
df = pd.DataFrame([[1, 2],[6,7],[3,4]],columns=['col1','col2'],index=['a','b','c'])
print df
print'-------------'