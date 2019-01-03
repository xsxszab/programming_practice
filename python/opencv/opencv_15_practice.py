#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:29:03 2018

@author: xsxsz
"""

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('chair.jpg',0)
ret, th0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
th=[th0,th1,th2,th3]
plt.figure(figsize=(12,5))
for i in range(4):
    plt.subplot(221+i)
    plt.imshow(th[i])

plt.figure()
th4=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,17,10)
plt.imshow(th4)
