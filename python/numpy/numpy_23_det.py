# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:11:51 2018

@author: Administrator
"""

import numpy as np
m=np.mat([[2,3,4],[1,2,3],[4,6,7]])
print m
print'---------'
print np.linalg.det(m)
print'---------'
m1=np.mat([[3,5,7],[1,2,3],[4,6,7]])
print m1
print'---------'
print np.linalg.det(m1)
print'---------'
m2=m.T
print m2
print'---------'
print np.linalg.det(m2)
print'---------'
m3=np.diag([2,2,3,4])
print m3
print'---------'
print np.linalg.det(m3)
print'---------'
m4=np.mat([[0,0,6],[0,2,0],[1,0,0]])
print m4
print'---------'
print np.linalg.det(m4)
print'---------'
m5=np.diag([2,3,4])
m5=np.mat(m5)
print m5
print'---------'
print np.linalg.det(m5)
print'---------'
m6=np.array([[2,3,4],[0,3,5],[0,0,4]])
print m6
print'---------'
print np.linalg.det(m6)
print'---------'
m7=np.array([[4,6,8],[0,3,5],[0,0,4]])
print m7
print'---------'
print np.linalg.det(m7)
print'---------'
m8=np.mat([[2,4],[6,5]])
print m8
print'---------'
print np.linalg.det(m8)
print'---------'
m9=np.array([[1,4],[3,5]])
m10=np.array([[1,4],[3,5]])
print np.linalg.det(m9)+np.linalg.det(m10)
print'---------'
print m7
print'---------'
m7[[0,1],:]=m7[[1,0],:]
print m7
print'---------'
m7[:,[0,1]]=m7[:,[1,0]]
print m7
print'---------'
