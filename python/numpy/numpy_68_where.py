#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:18:07 2019

@author: xsxsz
"""

import numpy as np

xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result=[(x if c else y) for x,y,c in zip(xarr,yarr,cond) ]
print(result)
print('---------------')
result=np.where(cond,xarr,yarr)
print(result)
print('---------------')
