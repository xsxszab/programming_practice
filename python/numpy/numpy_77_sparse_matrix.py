#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:06:36 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

mat=np.zeros((1000,1000),dtype=np.int32)
mat[::10,::5]=1
plt.matshow(mat)
plt.colorbar()
