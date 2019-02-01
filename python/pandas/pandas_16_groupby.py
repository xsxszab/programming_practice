#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:20:41 2019

@author: xsxsz
"""

import pandas as pd

idx=[101,101,101,102,102,102,103,103,103]
name=["apple","pearl","orange", "apple","pearl","orange","apple","pearl","orange"]
price=[1.0,2.0,3.0,4.00,5.0,6.0,7.0,8.0,9.0]
df1=pd.DataFrame({ "fruit": name, "price" : price, "supplier" :idx})
print(df1)
print('--------------')
dg1=df1.groupby('fruit')
for n,g in dg1:
    print('group name:',n,'\n|',g,'|')
print('--------------')
dg2=df1.groupby(['fruit','supplier'])
for n,g in dg2:
    print('group name:',n,'\n|',g,'|')
print('--------------')
si=df1.set_index(['fruit','price'])
print(si)
print('--------------')
