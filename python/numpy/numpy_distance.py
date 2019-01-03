# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:48:23 2018

@author: Administrator
"""

import numpy as np
import math
def Euclidean(vec1,vec2):
    nvec1=np.array(vec1)
    nvec2=np.array(vec2)
    return math.sqrt(((nvec1-nvec2)**2).sum())

a=[1,2]
b=[1,2]
print Euclidean(a,b)
print'-----------'
c=[0,0,0]
d=[2,3,4]
print Euclidean(c,d)
print'-----------'
def Manhattan(vec1,vec2):
    nvec1=np.array(vec1)
    nvec2=np.array(vec2)
    return np.abs(nvec1-nvec2).sum()
print Manhattan(a,b)
print'-----------'
print Manhattan(c,d)
print'-----------'
def Chebyshev(vec1,vec2):
    nvec1=np.array(vec1)
    nvec2=np.array(vec2)
    return max(np.abs(nvec1-nvec2))
print Chebyshev(a,b)
print'-----------'
print Chebyshev(c,d)
print'-----------'
def Minkowski(vec1,vec2,param):
   if param==1:
       return Manhattan(vec1,vec2)
   if param==2:
       return Euclidean(vec1,vec2)
   else:
       return Chebyshev(vec1,vec2)
print Minkowski(a,b,1)
print'-----------'
def Mahalanobis(vec1,vec2):
    return #以后再写
def cosine(vec1,vec2):
    return #以后再写
