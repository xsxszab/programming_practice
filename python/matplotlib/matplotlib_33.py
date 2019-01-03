#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:30:40 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
plt.figure(1,figsize=(6,5))
line=plt.plot([[1,2,3],[4,5,6]])[2]
line.set(color='k')
axis=plt.gca().xaxis
print(axis)
print('-----------')
print(axis.get_ticklines)
print('-----------')
for label in axis.get_ticklabels():  
    label.set_color('red')        
    label.set_rotation(30)   
    label.set_fontsize(16)    
for line in axis.get_ticklines():
    line.set(color='g',markersize=10,markeredgewidth=5)

