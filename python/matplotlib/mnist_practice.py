#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:31:47 2018

@author: xsxsz
"""

import os
import struct
import numpy as np
import matplotlib.pyplot as plt

#Not so clear........................
def load_mnist(kind='train'):
     labels_path = os.path.join('/resource/repository_python/mnist/','%s-labels-idx1-ubyte'% kind)
     images_path = os.path.join('/resource/repository_python/mnist/','%s-images-idx3-ubyte'% kind)
     with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

     with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        images = np.fromfile(imgpath,dtype=np.uint8).reshape(len(labels), 784)
     return images, labels
#....................................
images,labels=load_mnist()
print(images.shape)
print('------------')
print(labels.shape)
plt.figure(figsize=(12,10))
fig,ax=plt.subplots(nrows=2,ncols=2,sharex=True,sharey=True)
ax=ax.flatten()
images=images.reshape(60000,28,28)
for i in range(4):
    ax[i].imshow(images[i,:],cmap='gray')
    