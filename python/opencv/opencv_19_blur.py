#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:31:08 2018

@author: xsxsz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img0=cv2.imread('chair.jpg',0)
img1=cv2.blur(img0,(1,10))
img2=cv2.medianBlur(img0,5)
kernel=np.ones([5,5],np.float32)/20
img3=cv2.filter2D(img0,-1,kernel)
imgs=[img0,img1,img2,img3]
plt.figure(figsize=(12,10))
for i in range(4):
    plt.subplot(221+i)
    plt.imshow(imgs[i])

