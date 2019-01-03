#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:57:17 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import  preprocessing
mat=np.random.random((40,2))*10
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.scatter(mat[:,0],mat[:,1],color='g',alpha=0.8)
mat_processed=preprocessing.scale(mat)
plt.subplot(212)
plt.scatter(mat_processed[:,0],mat_processed[:,1],color='b',alpha=0.8)
