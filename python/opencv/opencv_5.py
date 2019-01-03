#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:06:16 2018

@author: xsxsz
"""

import numpy as np
import cv2
img=cv2.imread('image.png')
img_half=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
img_add=cv2.copyMakeBorder(img,50,50,20,0,cv2.BORDER_CONSTANT,value=(0,0,255))
cv2.imwrite('test1.png',img_half)
cv2.imwrite('test2.png',img_add)
img_patch=img[10:100,200:240,:]
cv2.imwrite('test3.png',img_patch)
