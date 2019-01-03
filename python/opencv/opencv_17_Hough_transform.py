#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:25:43 2018

@author: xsxsz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('chair.jpg')
drawing = np.zeros(img.shape[:], dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
lines = cv2.HoughLines(edges, 0.9, np.pi / 180, 90)

for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    cv2.line(drawing,(x1,y1),(x2,y2),(0,0,255))

plt.figure()
plt.imshow(drawing)

drawing = np.zeros(img.shape[:], dtype=np.uint8)
lines=cv2.HoughLinesP(edges,0.8,np.pi/180,90,minLineLength=50, maxLineGap=20)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(drawing,(x1,y1),(x2,y2),(0,255,0),1,lineType=cv2.LINE_AA)

plt.figure()
plt.imshow(drawing)
