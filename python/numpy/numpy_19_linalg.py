# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:45:51 2018

@author: Administrator
"""

import numpy as np
print np.linalg.info
print'----------'
a=[[1,-2,1],[0,2,-8],[-4,5,9]]
n=np.array(a)
print n
print'----------'
print np.linalg.det(n)
mat=np.mat(a)
print'----------'
print mat
print'----------'
print np.linalg.inv(mat)
print'----------'
b=np.array([0,8,9])
x= np.linalg.solve(mat,b)
print x
print'----------'
print np.dot(mat,x)
print'----------'
