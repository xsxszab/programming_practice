#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:40:21 2019

@author: xsxsz
"""

import numpy as np
a=np.mat(np.ones([2,4]))
b=np.mat(np.zeros([2,4]))
c=np.bmat('a,b;b,a')
print(c)
print('-------------')
d=np.tile(c,[3,2])
print(d)
print('-------------')
