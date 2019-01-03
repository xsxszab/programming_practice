# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:14:05 2018

@author: Administrator
"""

import numpy as np
a=[[1,2,3],[4,5,6]]
print a
print'-----------'
arr=np.stack(a)
print arr
print'-----------'
arr1=np.stack(a,axis=0)
print arr1
print'-----------'
arr2=np.stack(a,axis=1)
print arr2
print'-----------'
b=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12]]
arr3=np.stack(b)
print arr3
print'-----------'
arr4=np.stack(b,axis=0)
print arr4
print'-----------'
arr5=np.stack(b,axis=1)
print arr5
print'-----------'
c=[[1,2,2,2],[7,8,9,0],[4,5,4,2]]
print np.stack((b,c))
print'-----------'
print np.vstack((b,c))
print'-----------'
print np.hstack((b,c))