#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 18:29:37 2018

@author: xsxsz
"""

import numpy as np
arr=np.array([1,2,3,4])
print(np.pad(arr,pad_width=(1,2),mode='constant'))
print('------------')
print(np.pad(arr,pad_width=(1,1),mode='edge'))
print('------------')
