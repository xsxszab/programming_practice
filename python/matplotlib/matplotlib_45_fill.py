#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:24:17 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as  plt
x=np.linspace(-10,10,200)
y=np.sin(x)
plt.figure(figsize=(6,5))
plt.plot(x,y+1)
plt.fill_between(x,1.5,y+1,color='g',alpha=0.8)
plt.figure(figsize=(6,5))
plt.plot(x,y+1)
plt.fill_between(x,y+1,(y-1)>-1,color='b',alpha=0.8)
plt.fill_between(x,y+1,(y-1)<-1,facecolor='g',alpha=0.8)
