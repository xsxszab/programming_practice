#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:23:59 2018

@author: xsxsz
"""

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('scenery.jpg',0)
dst=cv2.equalizeHist(img)
plt.figure(0)
plt.imshow(dst)
clahe=cv2.createCLAHE(5,(8,8))
des=clahe.apply(img)
plt.figure(1)
plt.imshow(dst)
