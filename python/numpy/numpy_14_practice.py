# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:47:38 2018

@author: Administrator
"""

import numpy as np
list=np.empty((8,4))
print list
print'---------'
for i in range(8):
    list[i]=i
print list
print'---------'
print list[[4,3,0,6]]
print'---------'
print list[2]
print'---------'
print list[-2]
print'---------'
print list[2:4]
print'---------'
