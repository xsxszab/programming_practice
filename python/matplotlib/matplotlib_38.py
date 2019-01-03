#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:08:32 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
data=np.random.random((2,6))
plt.figure(figsize=(12,5))
plt.subplot(121)
plt.scatter(data[0,:],data[1,:])
plt.subplot(122)
for i in range(len(data[1,:])):
    plt.scatter(data[0,i],data[1,i])