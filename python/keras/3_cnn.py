#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:29:46 2019

@author: xsxsz
"""

import numpy as np
from keras.models import Sequential
from keras.layers import *

model=Sequential()
model.add(Conv2D(32,kernel_size=(5,5),strides=(1,1),activation='relu',input_shape=(200,200,3)))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(64,(5,5),activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(1000,activation='relu'))
model.add(Dense(20,activation='softmax'))
print(model.summary())