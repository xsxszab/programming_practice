#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:45:09 2018

@author: xsxsz
"""

import numpy as np
from sklearn import preprocessing
encoder=preprocessing.LabelEncoder()
classes=['a','d','hgfd','etrfg','f','t']
encoder.fit(classes)
print(encoder.classes_)
print('-----------')
for i,label in enumerate(encoder.classes_):
    print(i,label)
print('-----------')
inverse=encoder.inverse_transform([3,2])
print(inverse)
print('-----------')
