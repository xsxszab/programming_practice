 # -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:35:47 2018

@author: Administrator
"""

import numpy as np
list=[1,2,34,5,42,4,1,3,0,6,6,2]
list.sort()
print list
print'---------'
list1=np.array([12,3,5,6,3,77,787,8,6543])
print list1
print'---------'
print list1.argsort()
print'---------'
print list1.any()
print'---------'
print list1.all()
print'---------'
list2=[12,3,5,46,3,77,787,8,65443]
print (list1==list2)
print'---------'
a=(list1==list2)
print a
print'---------'
print a.any()
print'---------'
print a.all()
print list1.argmax()
print'---------'
print list1.argmin()
print'---------'
print list1.mean()
print'---------'
print list1.repeat(2)
print'---------'
mat=np.array(([2,21,3],[4,5,6]))
print mat
print'---------'
print mat.repeat(2)
print'---------'
print mat.repeat(2,0)
print'---------'
print mat.repeat(2,1)
print'---------'
print np.tile(mat,1)
print'---------'
print np.tile(mat,2)
print'---------'
print np.tile(mat,(2,2))