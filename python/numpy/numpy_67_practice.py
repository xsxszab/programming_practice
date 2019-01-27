#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 09:53:00 2019

@author: xsxsz
"""

import numpy as np

arr=np.arange(32).reshape((8,4))
ans=arr[np.ix_([5,6,4,7],[1,2,3,0])]

print(arr)
print('----------------')
print(ans)
print('----------------')
