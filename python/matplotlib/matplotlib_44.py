#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:33:01 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(6,5))
x=np.array([[0,0],[3,4],[5,6]])
y=np.array([[5,6],[3,2],[5,0]])
for i in range(len(x)):
    print(x[i])
    print('-------------')
    print(y[i])
    print('-------------')
    plt.plot(x[i],y[i])
    