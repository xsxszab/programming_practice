# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:51:02 2018

@author: Administrator
"""

import pandas as pd
df1=pd.DataFrame({'key':['b','b','a','a','b','a','c'],'data1':range(7)})
df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
print df1
print'-------------'
print df2
print'-------------'
print pd.merge(df1,df2)
print'-------------'
frame=pd.read_csv('data.csv',header=1)
print frame
print'-------------'
