#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:37:51 2018

@author: xsxsz
"""

import numpy as np
mat1=np.linspace(0,20,20,dtype='int').reshape(4,5)
print(mat1)
print('------------')
print(mat1.swapaxes(0,1))
print('------------')
mat2=np.arange(0,16,1).reshape(2,2,4)
print(mat2)
print('------------')
mat3=mat2.transpose(1,0,2)
print(mat3)
print('------------')
