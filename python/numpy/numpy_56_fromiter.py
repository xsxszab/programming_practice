#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:27:17 2018

@author: xsxsz
"""

import numpy as np

def generator():
    for x in range(20):
        yield x

arr=np.fromiter(generator(),dtype='int')
print(arr)
print('-----------')
