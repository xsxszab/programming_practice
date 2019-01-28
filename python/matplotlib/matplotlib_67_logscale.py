#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:57:27 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,1000,10000)
plt.figure(figsize=(6,12))
plt.subplot(311)
plt.plot(x,color='g')
plt.subplot(312)
plt.xscale('log')
plt.plot(x,color='b')
plt.subplot(313)
plt.yscale('log')
plt.plot(x,color='r')