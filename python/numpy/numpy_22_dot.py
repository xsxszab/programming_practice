# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:47:07 2018

@author: Administrator
"""

import numpy as np
mat1=[[1,0],[0,0]]
mat1=np.array(mat1)
vec=np.array([2,1])
vec=vec.T
print vec.dot(mat1)
print'---------'
vec2=np.array([1,2])
print'---------'
print vec2.dot(mat1)
print'---------'
mat2=np.linspace(0,20,20,dtype=int).reshape(4,5)
print mat2
print'---------'
print mat2.T
print'---------'
print mat2.T.T
print'---------'
mat3=np.linspace(30,40,20,dtype=int).reshape(5,4)
print mat3
print'---------'
print mat2.dot(mat3)
print'---------'
mat2=mat2.T
mat3=mat3.T
print mat3.dot(mat2)
print'---------'
mat4=np.eye(5)
print mat4
print'---------'
print (mat4==mat4.T)
mat5=np.linspace(20,90,36).reshape(6,6)
mat5[3][5]=0
mat6=np.linalg.inv(mat5)
print'---------'
print mat6.dot(mat5)
n=np.array([[-2,4],[1,-2]])
n1=np.array([[2,4],[-3,-6]])
print n.dot(n1)
print'---------'
print n1.dot(n)
print'---------'
