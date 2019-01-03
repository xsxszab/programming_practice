#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:58:37 2018

@author: xsxsz
"""

import numpy as np
rand=np.random.RandomState(10)
label=(rand.rand(10)*10).astype('int')
print(label)
print('----------------')
print(label.reshape(-1))
print('----------------')
temp=np.eye(8)[label.reshape(-1)].T
print(temp)
print('----------------')
