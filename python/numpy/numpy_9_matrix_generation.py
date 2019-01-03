# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 08:38:03 2018

@author: Administrator
"""

import numpy as np
a=np.full((4,4),2)
print a
print'--------------'
b=np.diag([1,42,6],k=-1)
print b
print'--------------'
print a*b
print'--------------'
print np.dot(a,b)
print'--------------'
print np.diag(a)
print'--------------'
c=np.ones_like(a)
print c
print'--------------'
a=np.sqrt(a)
print a
print'--------------'
print np.exp(a)
print'--------------'
print np.sign(a)
print'--------------'
d=np.full((4,4),-1)
print np.copysign(a,d)
np.savetxt('numpytest9.csv',a,fmt='%d',delimiter=',')