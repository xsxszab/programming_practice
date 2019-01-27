#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:49:21 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

num=1000
draws = np.random.randint(0, 2, size=num)
steps=np.where(draws>0,1,-1)
walk=steps.cumsum()
x=np.arange(1,1001,1)
plt.plot(x,walk,color="g")
plt.xlim(0,1000)
plt.plot(x,np.zeros_like(x),"--",color="b")
plt.title('walk')
