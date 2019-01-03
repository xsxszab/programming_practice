#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:34:57 2018

@author: xsxsz
"""

import numpy as np
mat=np.array([[1,2,3,4],[9,0,8,7],[5,6,7,8]])
print(mat)
print('---------')
print(np.linalg.cond(mat))
print('---------')
print(np.linalg.svd(mat))
print('---------')
print(np.linalg.pinv(mat))
print('---------')
print(np.trace(mat))
print('---------')
