#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:46:29 2018

@author: xsxsz
"""

import os
import time
import sys
import numpy as np
import cv2 as cv

interval=1
frame_number=50
fps=24

camera=cv.VideoCapture(0)
size=(int(camera.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(camera.get(cv.CAP_PROP_FRAME_HEIGHT)))
video=cv.VideoWriter('save.avi',cv.VideoWriter_fourcc('M', 'P', '4', '2'),fps,size)

try:
    for i in range(frame_number):
        _,frame=camera.read()
        video.write(frame)
        time.sleep(interval)

except KeyboardInterrupt:
    print('stopped')

video.release()
camera.release()