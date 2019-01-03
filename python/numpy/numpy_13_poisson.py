# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:42:34 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
y=np.random.normal(3,0.1,10000)
print y
print'-------------------'
plt.hist(y,bins=100,normed=True,color='g')
plt.figure()
y1=np.random.poisson(20,size=10000)
plt.hist(y1,bins=100)