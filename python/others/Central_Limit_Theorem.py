#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:43:17 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import math
u=0;
sig=0.05
t=10000
a=np.zeros(1000)
for i in range(t):
    a+=np.random.uniform(-5,5,1000)
a=(a-u)/(sig/math.sqrt(t))

plt.figure(figsize=(5,6))
plt.title('Central_Limit_Theorem')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(alpha=0.75)
plt.hist(a,bins=30,alpha=0.8,color='g')
