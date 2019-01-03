#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:56:42 2018

@author: xsxsz
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('flower.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift=cv.xfeatures2d.SIFT_create()
kp=sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('sift.png',img)