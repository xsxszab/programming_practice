#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:31:54 2018

@author: xsxsz
"""

import numpy as np
import cv2 as cv
canvas=np.zeros([400,600,3],dtype=np.uint8)+255
cv.line(canvas,(100,0),(100,599),(0,255,0),2)
cv.circle(canvas,(150,200),80,(200,45,78),2)
cv.rectangle(canvas,(0,0),(200,300),(0,0,0),2)
triangles=np.array([
    [(200, 240), (145, 333), (255, 333)],
    [(60, 180), (20, 237), (100, 237)]])
cv.fillPoly(canvas,triangles,(0,255,255))
cv.putText(canvas,
            'haha',
            (5, 15),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 0),
            1)
cv.imwrite('test.png',canvas)
