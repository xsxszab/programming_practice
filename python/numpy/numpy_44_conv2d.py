#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 18:57:50 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

img=plt.imread('chair.jpg')

kernel=np.zeros([3,3,3])
kernel[0]=kernel[1]=kernel[2]=[[1,0,-1],[1,0,-1],[1,0,-1]]
def conv2d(img,kernel,stride=1):
    output=np.zeros([img.shape[0]-kernel.shape[1]+1,img.shape[1]-kernel.shape[2]+1,kernel.shape[0]])
    for i in range(3):
        current_kernel=kernel[i,:,:]
        for j in range(output.shape[0]):
            for k in range(output.shape[1]):
                conv=current_kernel*img[j:j+3,k:k+3,i]
                output[j][k][i]+=np.sum(conv)
    return output

conv=conv2d(img,kernel=kernel)
plt.figure(0)
plt.imshow(conv)
