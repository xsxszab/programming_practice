# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:58:19 2018

@author: Administrator
"""

import numpy as np
arr=np.arange(4).reshape((2,2))
print arr
print'---------'
arr1=np.transpose(arr)
print arr1
print'---------'
arr2=np.linspace(1,10,10,dtype=int)
print arr2
print'---------'
arr3=np.transpose(arr2)
print arr3
arr2.shape=(2,5)
print arr2
print'---------'
print arr2.shape[0],arr2.shape[1]