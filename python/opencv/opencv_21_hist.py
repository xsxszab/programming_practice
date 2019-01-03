#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:06:14 2018

@author: xsxsz
"""

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('scenery.jpg')
color=('r','g','b')
plt.figure(0)
plt.imshow(img)
plt.figure(1)
plt.hist(img.ravel(),256,[0,256])
plt.figure(2)
for i,color in enumerate(color):
    hist=cv2.calcHist(images=[img],channels=[i],mask=None,histSize=[256],ranges=[0,256])
    plt.plot(hist,color)
