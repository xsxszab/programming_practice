#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:08:00 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
num=100
x=np.random.rand(num)
y=np.random.rand(num)
max_radius=25
area=np.pi*(max_radius*np.random.rand(num))**2
colors=np.random.rand(num)
plt.scatter(x,y,c=colors,s=area,alpha=0.1)
