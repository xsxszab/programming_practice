#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:46:00 2018

@author: xsxsz
"""

import cv2
import matplotlib.pyplot as plt

flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
for i in flags:
    print(i)
print('------------')
img=cv2.imread('chair.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('img_gray.png',img_gray)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print(img_hsv.shape)
print('------------')
