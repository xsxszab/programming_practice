#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:25:46 2019

@author: xsxsz
"""

import numpy as np

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
zz=zip(a,b,c)
print(zz)
x,y,z=zip(*zz)
print(x)
print(y)
print(z)
print('-----------------')