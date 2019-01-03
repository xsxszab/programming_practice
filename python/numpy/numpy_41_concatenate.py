#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:10:43 2018

@author: xsxsz
"""

import numpy as np
mat1=np.linspace(0,100,20,dtype='int').reshape(2,10)
mat2=np.linspace(0,100,10,dtype='int').reshape(1,10)
print(mat1.shape)
print('---------------')
print(mat2.shape)
print('---------------')
mat3=np.concatenate((mat1,mat2),axis=0)
print(mat3.shape)
print('---------------')
