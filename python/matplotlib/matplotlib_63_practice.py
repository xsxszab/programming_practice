#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:20:39 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

t=range(1000)
y=[np.sqrt(i) for i in t]
plt.plot(t,y)
plt.fill_between(t,y,color='silver')
plt.xlim(0,1000)
plt.ylim(0,32)
