# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:54:38 2018

@author: Administrator
"""

import numpy as np
a=np.array([[2,3],[4,5]])
b=np.array([[1,2],[3,4]])
print a.dot(b)
print'--------'
print np.tile(a,2)
print'--------'
print np.tile(a,(2,1))
print'--------'
print a.shape[0]
print'--------'
c=np.linspace(1,100,24,dtype=int).reshape(2,3,4)
print c
print'--------'
print c.shape[0]
print'--------'
print c.shape[1]
print'--------'
print c.shape[2]
print'--------'
