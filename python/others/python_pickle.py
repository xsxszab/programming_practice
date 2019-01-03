#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:16:57 2018

@author: xsxsz
"""

import pickle
datalist = [[1, 1, 'yes'],  
            [1, 1, 'yes'],  
            [1, 0, 'no'],  
            [0, 1, 'no'],  
            [0, 1, 'no']]  
datadic = { 0: [1, 2, 3, 4],  
            1: ('a', 'b'),  
            2: {'c':'yes','d':'no'}}
fw=open('data.dat','wb')
pickle.dump(datalist,fw,-1)
pickle.dump(datadic,fw)
fw.close()

fr=open('data.dat','rb')
print(fr)
print('----------')
print(type(fr))
print('----------')
data1=pickle.load(fr)
print(data1)
print('----------')
data2=pickle.load(fr)
print(data2)
print('----------')
