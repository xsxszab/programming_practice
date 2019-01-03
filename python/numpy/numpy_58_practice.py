#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:30:27 2018

@author: xsxsz
"""

import numpy as np

arr=np.linspace(10,20,20,dtype='int').reshape(2,10)
print(arr)
print('-----------')
arr[[0,1]]=arr[[1,0]]
print(arr)
print('-----------')
