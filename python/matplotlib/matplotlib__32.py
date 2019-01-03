#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:14:40 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
plt.figure(1,figsize=(6,5))
line=plt.plot(range(5))[0]
print(line)
print('-------')
line.set_color('g')
line.set_linewidth(6)
plt.getp(line)
print('-------')
plt.figure(2,figsize=(6,5))
for i,color in enumerate('rgbyck'):
    plt.subplot(231+i)
    ax=plt.gca()
    ax.patch.set(facecolor=color,alpha=0.8)