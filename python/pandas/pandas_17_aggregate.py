#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:29:08 2019

@author: xsxsz
"""

import numpy as np
import pandas as pd

idx=[101,101,101,102,102,102,103,103,103]
idx+=[101,102,103]
name=["apple","pearl","orange", "apple","pearl","orange","apple","pearl","orange"]
name+=["apple"] * 3
price=[1.0,2.0,3.0,4.00,5.0,6.0,7.0,8.0,9.0]
price+=[4] * 3
df1=pd.DataFrame({ "fruit": name, "price" : price, "supplier" :idx})
print(df1)
print('------------')
dg1=df1.groupby(["fruit", "supplier"])
for n, g in dg1:
    print("multiGroup on:",n,"\n|",g,"|")
print('------------')
print(dg1.agg(np.mean))
print('------------')
print(dg1.agg([np.mean,np.std,np.min,np.sum,np.max]))
print('------------')
