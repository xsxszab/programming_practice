#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:16:30 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
img=cv2.imread('chair.jpg',0)
ret,th=cv2.threshold(img,128,255,cv2.THRESH_BINARY)
print(type(ret))
print('------------')
print(type(th))
print('------------')
print(ret)
print('------------')
cv2.imwrite('binary.png',th)
