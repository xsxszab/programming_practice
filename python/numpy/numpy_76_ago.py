#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:30:48 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

x0=np.arange(1,21,1)
plt.plot(x0,color='g')
plt.xlim(0,20)
def AGO(x):
    temp=x[0]
    arr=[temp]
    for i in range(1,len(x)):
        temp+=x[i]
        arr.append(temp)
    return arr

x1=AGO(x0)
x2=AGO(x1)
plt.plot(x1,color='b')
plt.plot(x2,color='r')
plt.title('AGO')
