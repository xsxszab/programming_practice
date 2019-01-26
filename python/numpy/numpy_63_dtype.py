#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:19:16 2019

@author: xsxsz
"""

import numpy as np

mytype=np.dtype({'names':['name','age','class'],'formats':['S32','i', 'f']})
typelist=np.array([('a',18,2),('b',18,2)],dtype=mytype)
print(typelist.dtype)
print('------------------')
print(typelist[0]['name'])
print(typelist[1]['name'])
print(typelist.strides)
typelist.tofile("test.dats")