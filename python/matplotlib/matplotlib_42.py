#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:23:19 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
rand=np.random.RandomState(1)
mat=np.linspace(-10,10,100).reshape((10,10))+rand.rand(10,10)
print(mat)
print('-------------')
plt.figure(figsize=(6,5))
plt.matshow(mat,cmap='rainbow')