#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:21:09 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
a=np.array([100,2,12,34,47,24,12,4,7,0.1])
print(a)
print('-------')
plt.subplot(121)
plt.plot(a)
print(preprocessing.scale(a))
print('-------')
plt.subplot(122)
plt.plot(preprocessing.scale(a))
