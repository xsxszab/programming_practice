#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:31:39 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,5,0.1)
lines = plt.plot(x, np.sin(x), x, np.cos(x))
plt.setp(lines,color="g",linewidth=1.5)
print(lines[0].get_linewidth())
print('-------------------')
print(plt.getp(lines[1]))
print('-------------------')
f=plt.gcf()
print(f)
print('-------------------')
print(plt.getp(f))
print('-------------------')
print(plt.gca())
print('-------------------')
