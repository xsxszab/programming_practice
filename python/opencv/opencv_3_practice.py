#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:50:07 2018

@author: xsxsz
"""

import numpy as np
import cv2
img=cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('image_opencv.png',img)
