#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:52:10 2018

@author: xsxsz
"""

import numpy as np
mat=np.linspace(-10,10,24,dtype='int').reshape(2,3,4)
print(mat.shape)
print('---------')
print(mat)
print('---------')
print(mat[:,:,1:-1])
print('---------')
print(mat[1,1,1])
print('---------')
print(mat[1,1,[2,3]])
print('---------')
print(mat[[1,1],[2,0]])
print('---------')
print(mat[[0,1],[2,1]])
print('---------')
print(mat[[0,1],[2,1],[1,2]])
print('---------')
print(mat[[0,1],[2,1],[1]])
print('---------')
