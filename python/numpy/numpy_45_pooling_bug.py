#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:44:33 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

size=[2,2]
img=plt.imread('chair.jpg')

def max_pooling(img,size,stride=2):
    output=np.zeros([int(img.shape[0]/stride),int(img.shape[1]/stride),img.shape[2]])
    for i in  range(3):
        r=0
        for j in np.arange(0,img.shape[0]+1,2):
            c=0
            for k in np.arange(0,img.shape[1]+1,2):
                output[r][c][i]=np.max(img[j:j+2,k:k+2,i])
                c++1
            r+=1    
    return output

pic=max_pooling(img,size)
plt.figure(0)
plt.imshow(pic)
