#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:07:32 2019

@author: xsxsz
"""

import pandas as pd

df1=pd.DataFrame({'key':['b','b','a','a','b','a','c'],'data1':range(7)})
df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
print(df1)
print('--------------')
print(df2)
print('--------------')
print(pd.merge(df1,df2,on='key'))
print('----------------------------')
df3=pd.DataFrame({'key1':['b','b','a','a','b','a','c'],'key2':['i','j','k','k','i','j','k'],'data1':range(7)})
df4=pd.DataFrame({'key1':['a','b','d'],'key2':['k','j','i'],'data2':range(3)})
print(df3)
print('--------------')
print(df4)
print('--------------')
print(pd.merge(df3,df4,on=['key1','key2']))
print('----------------------------')
df5=pd.DataFrame({'l_key':['b','b','a','a','b','a','c'],'data1':range(7)})
df6=pd.DataFrame({'r_key':['a','b','d'],'data2':range(3)})
print(df5)
print('--------------')
print(df6)
print('--------------')
print(pd.merge(df5,df6,left_on='l_key',right_on='r_key'))
print('----------------------------')
print(df1)
print('--------------')
print(df2)
print('--------------')
print(pd.merge(df1,df2,on='key',how='outer'))
print('--------------')
print(pd.merge(df1,df2,on='key',how='inner'))
print('--------------')
print(pd.merge(df1,df2,on='key',how='left'))
print('--------------')
print(pd.merge(df1,df2,on='key',how='right'))
print('----------------------------')
