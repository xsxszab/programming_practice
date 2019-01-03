# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:22:41 2018

@author: Administrator
"""

import numpy as np
import time
a=np.random.rand(100000)
b=np.random.rand(100000)
time1=time.time()*1000
c=np.dot(a,b)
time2=time.time()*1000
c=0
for i in range(100000):
   c+=a[i]*b[i]
time3=time.time()*1000
print time2-time1
print'---------------'
print time3-time2