#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:45:44 2018

@author: xsxsz
"""

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('scenery.jpg')
plt.figure(0)
plt.imshow(img)
img1=cv2.GaussianBlur(src=img,ksize=(15,15),sigmaX=0,)
plt.figure(1)
plt.imshow(img1)
