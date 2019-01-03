#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:54:38 2018

@author: xsxsz
"""

import numpy as np
import cv2
img=cv2.imread('image.png')
print(img.shape)
print('----------')
print(img.dtype)
print('----------')
img[:,:,2]=0
cv2.imwrite('img_opencv.png',img)
