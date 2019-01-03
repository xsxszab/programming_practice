#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:29:40 2018

@author: xsxsz
"""

import numpy as np
a=np.linspace(0,20,15,dtype='int').reshape(3,5)
print(a)
print('---------')
print(a[:,1])
print('---------')
print(a[0,:])
print('---------')
print(a[:,::2])
print('---------')
print(a[a%2==0])
print('---------')
b=a>4
print(b)
print('---------')
a[b]=-1
print(a)
print('---------')
print(a+10)
print('---------')
a=np.random.randint(1,10,size=(3,4))
print(a)
print('---------')
b=np.sort(a)
print(b)
print('---------')
b=np.sort(a,axis=0)
print(b)
print('---------')
b=np.sort(a,axis=1)
print(b)
print('---------')
