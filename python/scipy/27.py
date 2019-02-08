#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 17:05:16 2019

@author: xsxsz
"""

import numpy as np
from scipy import linalg

mat1=np.mat('[1 5 2; 2 4 1; 3 6 2]')
print(mat1)
print('-----------------')
la,v=linalg.eig(mat1)
print(la)
print('-----------------')
print(v)
print('-----------------')
