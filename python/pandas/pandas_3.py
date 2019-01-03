# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:51:09 2018

@author: Administrator
"""

import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
DataSet=list(zip(names,births))
print DataSet
print'------------------'
df = pd.DataFrame(data = DataSet, columns=['Names', 'Births'])
print df
print'------------------'
df.to_csv('data.csv',index=False,header=False)
df1=pd.read_csv('data.csv')
print df1
