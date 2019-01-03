#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:32:06 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.random.random(size=(40,600))
plt.figure(figsize=(12,10))
plt.subplot(221)
color=np.arctan2(x[0,:],x[1,:])
plt.scatter(x[0,:],x[1,:],c=color)
x=x-np.mean(x)
plt.subplot(222)
color=np.arctan2(x[0,:],x[1,:])
plt.scatter(x[0,:],x[1,:],c=color)
plt.subplot(223)
x/=np.std(x,axis=0)
color=np.arctan2(x[0,:],x[1,:])
plt.scatter(x[0,:],x[1,:],c=color)
plt.subplot(224)
