#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:40:32 2018

@author: xsxsz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv

rand=np.random.RandomState(10)
def gaussian_noise(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            s=rand.normal(0,20,3)
            b=img[i,j,0]
            g=img[i,j,1]
            r=img[i,j,2]
            img[i,j,0]=clamp(b+s[0])
            img[i,j,1]=clamp(g+s[1])
            img[i,j,2]=clamp(r+s[2])
            plt.imshow(img)

img=cv2.imread('scenery.jpg')
plt.figure(0)
plt.imshow(img)
plt.figure(1)
gaussian_noise(img)
