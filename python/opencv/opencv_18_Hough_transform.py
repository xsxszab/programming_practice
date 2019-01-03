#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:21:02 2018

@author: xsxsz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('ball.jpg')
drawing=np.zeros(img.shape[:],dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
#plt.imshow(edges)
circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,10,param2=20)
circles = np.int0(np.around(circles))
for i in circles[0, :]:
    cv2.circle(drawing, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(drawing, (i[0], i[1]), 2, (0, 0, 255), 3)

plt.imshow(drawing)