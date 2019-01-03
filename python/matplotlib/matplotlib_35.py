#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:50:43 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
img=plt.imread('image.png')
print(img.shape)
print('-------------')
print(img.dtype)
print('-------------')

plt.xkcd()
plt.figure(figsize=(10,8))
plt.subplot(221)
plt.imshow(img)
plt.colorbar()
plt.subplot(222)
plt.imshow(img[:,:,0])
plt.colorbar()
plt.subplot(223)
plt.imshow(img[:,:,1])
plt.colorbar()
plt.subplot(224)
plt.colorbar()
plt.imshow(img[:,:,2])
