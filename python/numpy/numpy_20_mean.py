#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:05:55 2018

@author: xsxsz
"""

import numpy as np
mat=np.linspace(0,20,20,dtype='int').reshape(2,10)
print(mat)
print('------------')
mean1=np.mean(mat)
print(mean1)
print('------------')
mean2=np.mean(mat,axis=0)
print(mean2)
print('------------')
mean3=np.mean(mat,axis=1)
print(mean3)
print('------------')
