#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:40:52 2018

@author: xsxsz
"""

import numpy as np
import cv2
import os
random=bytearray(os.urandom(120000))
flat=np.array(random)
img=flat.reshape(300,400)
cv2.imwrite('opencv_test_1.png',img)
img=img.reshape(100,400,3)
cv2.imwrite('opencv_test_2.png',img)
