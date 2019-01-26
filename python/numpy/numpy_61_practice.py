#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:01:57 2019

@author: xsxsz
"""

import numpy as np
s="abcdef"
arr1=np.fromstring(s,dtype=np.int8)
print(arr1)
arr2=np.fromstring(s,dtype=np.int16)
