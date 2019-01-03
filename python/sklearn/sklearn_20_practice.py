#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:19:36 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
dia=load_diabetes()
data=dia.data
targets=dia.target
print(data.shape)
print('------------')
print(targets.shape)
print('------------')

'''
for i in range(442):
    plt.scatter(i+1,label_removemean[i])
plt.plot([0,442],[0,0],color='k')
'''

tar_mean=np.mean(targets)
label_removemean=targets-np.mean(targets)

label_color=[]
for i in range(442):
    if label_removemean[i]>=0:
        label_removemean[i]=1
        label_color.append('g')
    else:
        label_removemean[i]=0
        label_color.append('r')
'''        
for i in range(442):
    plt.scatter((i+1),label_removemean[i])
'''    

plt.figure(figsize=(12,22))
for i in range(442):
    plt.subplot(421)
    plt.scatter(i+1,data[i,0],color=label_color[i])
    plt.subplot(422)
    plt.scatter(i+1,data[i,1],color=label_color[i])
    plt.subplot(423)
    plt.scatter(i+1,data[i,2],color=label_color[i])
    plt.subplot(424)
    plt.scatter(i+1,data[i,3],color=label_color[i])
    plt.subplot(425)
    plt.scatter(i+1,data[i,4],color=label_color[i])
    plt.subplot(426)
    plt.scatter(i+1,data[i,5],color=label_color[i])
    plt.subplot(427)
    plt.scatter(i+1,data[i,6],color=label_color[i])
    plt.subplot(428)
    plt.scatter(i+1,data[i,7],color=label_color[i])
