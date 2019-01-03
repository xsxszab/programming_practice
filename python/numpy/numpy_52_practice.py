#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:12:33 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

mat=np.zeros([8,8])
mat[::2,::2]=1
mat[1::2,1::2]=1
print(mat)
print('---------')
plt.imshow(mat)
plt.colorbar()
