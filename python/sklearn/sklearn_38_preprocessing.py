#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:54:30 2019

@author: xsxsz
"""

import numpy as np
from sklearn import preprocessing as pre

x= np.array([[ 1., -1.,  2.],
             [ 2.,  0.,  0.],
             [ 0.,  1., -1.]])
scaled=pre.scale(x)
print(scaled)
print('--------------')
print(scaled.mean(axis=0))
print('--------------')
print(scaled.std(axis=0))
print('--------------')
scaler=pre.StandardScaler().fit(x)
print(scaler.mean_)
print('--------------')
print(scaler.scale_)
print('--------------')
print(scaler.var_)
print('--------------')
print(scaler.transform(x))
print('--------------')
print(scaler.get_params())
print('--------------')
reslut=scaler.inverse_transform(scaler.transform(x))
print(reslut)
print('--------------')
