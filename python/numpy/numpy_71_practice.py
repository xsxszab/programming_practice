#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:41:07 2019

@author: xsxsz
"""

import numpy as np

arr=np.random.randn(100).reshape(10,10)
arr=(arr>0)
print(arr)
print('---------------')
print(arr.sum())
print('---------------')
print(arr.any())
print('---------------')
print(arr.all())
print('---------------')
