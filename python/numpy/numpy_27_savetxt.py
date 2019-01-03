# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:47:00 2018

@author: Administrator
"""

import numpy as np
a=np.arange(40).reshape(10,4)
print(a)
np.savetxt('a.txt',a,fmt='%d',delimiter='.')
b=np.loadtxt('a.txt',dtype=int,delimiter='.')
print(b)
x,y,z=np.loadtxt('a.txt',dtype=int,delimiter='.',usecols=(0,2,3),unpack=True)
print(x)
print(y)
print(z)
