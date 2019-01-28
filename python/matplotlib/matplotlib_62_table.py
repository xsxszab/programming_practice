#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:15:38 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure()
ax=plt.gca()
y=np.random.randn(9)
rows=['row1','row2','row3']
cols=['col1','col2','col3']
values=[[11,12,13],[21,22,23],[31,32,33]]
colors=['red','gold','green']
table=plt.table(cellText=values,colWidths=[0.1]*3,rowLabels=rows,colLabels=cols,rowColours=colors,loc='upper right')
plt.plot(y,color='g')
