#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:14:35 2018

@author: xsxsz
"""
import numpy as np
import cv2
img=cv2.imread('sample.jpg',cv2.IMREAD_GRAYSCALE)
print(img.shape)
print('---------')
mat1=np.array([[1.5,0,-150],[0,1.5,-240]])
img1=cv2.warpAffine(img,mat1,(img.shape[0],img.shape[1]))
cv2.imwrite('sample_transformed_1.png',img1)
theta=15*np.pi/180
mat2=np.array([[1,np.tan(theta),0],[0,1,0]])
img2=cv2.warpAffine(img,mat2,(img.shape[0],img.shape[1]))
cv2.imwrite('sample_transformed_2.png',img2)
mat3=np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0]])
img3=cv2.warpAffine(img,mat3,(img.shape[0],img.shape[1]))
cv2.imwrite('sample_transformed_3.png',img3)
