#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 07:34:13 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
fig=plt.figure()
fig.patch.set_color('g')
fig.canvas.draw()
ax=fig.add_axes([0,0,0.6,0.5])
line=ax.plot([0,1],[0,1])
print(line)
print('--------')
print(type(line))
print('--------')
line[0].set(alpha=0.8,lw=4)
