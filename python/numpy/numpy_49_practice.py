#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:01:40 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

mat=np.zeros([6,6])
print(mat)
print('---------')
mat[[0,5]]=1
mat[:,[0,5]]=1
print(mat)
print('---------')
plt.imshow(mat)
plt.colorbar()
