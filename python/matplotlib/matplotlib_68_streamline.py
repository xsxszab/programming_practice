#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:05:06 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

y,x=np.mgrid[0:5:100j,0:5:100j]
u,v=x,y
plt.streamplot(x,y,u,v,color='g')
