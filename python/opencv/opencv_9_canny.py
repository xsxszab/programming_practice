#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:49:49 2018

@author: xsxsz
"""

import numpy as np
import cv2 as cv
img=cv.imread('chair.jpg')
print(img.shape)
print('----------')
img1=cv.Canny(img,100,100)
print(img1.shape)
print('----------')
cv.imwrite('char_canny.png',img1)