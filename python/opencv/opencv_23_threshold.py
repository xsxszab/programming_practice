#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:42:24 2018

@author: xsxsz
"""

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('scenery.jpg',0)
ret1,th1=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret2,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur=cv2.GaussianBlur(img,(15,15),0)
ret3,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
images = [img,0,th1,img,0,th2,blur,0,th3]
titles = ['Original','Histogram','Global(v=100)',
          'Original','Histogram',"Otsu's",
          'Gaussian filtered Image','Histogram',"Otsu's"]

for i in range(3):
    plt.subplot(331+i*3)
    plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3],fontsize=8)
    plt.xticks([]),plt.yticks([])

    plt.subplot(332+i*3)
    plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1],fontsize=8)
    plt.xticks([]),plt.yticks([])

    plt.subplot(333+i*3)
    plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2],fontsize=8)
    plt.xticks([]),plt.yticks([])

