#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:20:47 2018

@author: xsxsz
"""

import numpy as np
import cv2 as cv
img=cv.imread('flower.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(gray.shape)
print('---------')
surf=cv.xfeatures2d.SURF_create()
feature=surf.detect(gray)
img=cv.drawKeypoints(gray,feature,img)
cv.imwrite('surf.png',img)