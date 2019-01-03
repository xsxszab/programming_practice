#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:57:21 2018

@author: xsxsz
"""

import numpy as np
from sklearn import preprocessing
data=np.array([[3,-1,2,5],[0,4,-0.4,2.2],[1,3.4,-2,8]])
print(data)
print('-----------')
standardized=preprocessing.scale(data)
print(standardized)
print('-----------')
print(np.mean(standardized,axis=0))
print('-----------')
scaler=preprocessing.MinMaxScaler(feature_range=(0,2))
data_scaled=scaler.fit_transform(data)
print(data_scaled)
print('-----------')
data_normalized_l1=preprocessing.normalize(data,norm='l1')
print(data_normalized_l1)
print('-----------')
data_normalized_l2=preprocessing.normalize(data,norm='l2')
print(data_normalized_l2)
print('-----------')
binarize=preprocessing.Binarizer(threshold=0.5)
print(binarize.transform(data))
print('-----------')
