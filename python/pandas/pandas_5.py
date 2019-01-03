# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:36:56 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
dat=[[2,1,np.NaN,0],[-5,6,7,4],[5,np.nan,4,9],[6,np.NAN,3,2]]
index=['a','p','r','c']
a=pd.DataFrame(dat,index=index)
print a
print'-------'
print a.sum()
print'-------'
print a.sum(axis=0)
print'-------'
print a.sum(axis=1)
print'-------'
print a.sum(axis=0,skipna=False)
print'-------'
print a.mean()
print'-------'
print a.mean(axis=1)
print'-------'
print a.max()
print'-------'
print a.max(axis=1)
print'-------'
print a.max(axis=1,skipna=False)
print'-------'
print a.min()
print'-------'
print a.min(axis=1)
print'-------'
print a.min(axis=1,skipna=False)
print'-------'
print a.idxmin()
print'-------'
print a.cumsum()
print'-------'
print a.cummax()
print'-------'
print a.mad()
print'-------'
print a.mad(axis=1)
print'-------'
print a.var()
print'-------'
print a.std()
print'-------'
print a.abs()
print'-------'
print a.diff()
print'-------'
print a.pct_change()
print'-------'
print a.corr()
print'-------'
print a.sort_index()
print'-------'
