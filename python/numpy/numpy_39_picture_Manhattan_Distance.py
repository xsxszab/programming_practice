#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:06:10 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
img1=plt.imread('1.png')
img2=plt.imread('2.png')
diff=np.abs(img1-img2)
distance=np.sum(diff)
print(distance)
print('------------')
