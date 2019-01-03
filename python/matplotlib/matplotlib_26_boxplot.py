# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:52:57 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
data=np.random.rand(100)
plt.figure(figsize=(5,5))
plt.boxplot(data,sym='o')
plt.figure(figsize=(5,5))
np.random.seed(200)
data1=np.random.normal(size=(1000,4) , loc = 0 , scale=1)
label=['a','b','c','d']
plt.boxplot(data1,labels=label)