#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:23:28 2018

@author: xsxsz
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('flower.jpg',cv.IMREAD_GRAYSCALE)
print(img.shape)
print('----------')
ret,thre=cv.threshold(img,120,255,cv.THRESH_BINARY)
plt.imshow(thre)
ret,thre=cv.threshold(img,120,255,cv.THRESH_BINARY_INV)
plt.imshow(thre)
