#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:24:25 2019

@author: xsxsz
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

model=Sequential()
print(model)
print('---------------')
model.add(Dense(input_dim=1,units=1))
model.add(Dense(input_dim=1,units=1))
print(model.summary())