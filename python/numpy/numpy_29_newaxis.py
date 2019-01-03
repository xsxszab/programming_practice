#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 07:57:42 2018

@author: xsxsz
"""

import numpy as np
a=np.array([1,2,3,4,5,6])
b=a[np.newaxis]
print(a)
print('---------')
print(b)
print('---------')
print(np.transpose(a))
print('---------')
print(np.transpose(b))
print('---------')
c=a[None]
print(c)
print('---------')
d=a[:,np.newaxis]
print('---------')
print(d)
print('---------')
print(a.shape,b.shape,c.shape,d.shape)
a1=np.linspace(10,100,20,dtype=int).reshape(2,10)
print(a1)
print('---------')

b1=a1[np.newaxis]
print(b1)
print('---------')

print(a1.shape,b1.shape)
print('---------')
c1=a1[:,np.newaxis]
print(c1.shape)
print('---------')
d1=a1[:,:,np.newaxis]
print(d1.shape)
print('---------')
