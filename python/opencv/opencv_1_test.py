#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:30:46 2018

@author: xsxsz
"""

import numpy as np
import cv2

img=np.zeros((3,3),dtype=np.uint8)
img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(type(img))
print('----------')
print(img.shape)
print('----------')
