#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:28:49 2018

@author: xsxsz
"""

import numpy as np

arr=np.random.randint(0,5,size=(20))
print(arr)
print('-----------')
print(np.bincount(arr))
print('-----------')
