#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 07:57:18 2018

@author: xsxsz
"""

import numpy as np

list1=np.linspace(0,9,10,dtype='int')
print([i*10 for i in list1])
print('--------------')
print([i*10 for i in list1 if i>2])
print('--------------')
print([(i,i+1) for i in list1 ])
print('--------------')
