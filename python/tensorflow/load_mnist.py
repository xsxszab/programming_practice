#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:35:38 2018

@author: xsxsz
"""

import os
import struct
import numpy as np
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

