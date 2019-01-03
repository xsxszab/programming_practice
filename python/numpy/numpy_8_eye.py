# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:43:08 2018

@author: Administrator
"""
import numpy as np
data=[1,2,3,4,5,6,7,8,9,0]
map=eye(5,k=-1)
print map
print'-------'
map1=diag([1,2,3,4],k=1)
print map1
print'-------'
print map*map1
print'-------'
print np.dot(map,map1)