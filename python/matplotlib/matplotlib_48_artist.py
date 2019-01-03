#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 07:19:31 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0, 0, 0.6, 0.4])
ax.set_xlabel('x_label_here')
ax.set_ylabel('y_label_here')
line1=ax.plot([0,1,2,4],[1,2,1,2],c='g')
line2=ax.plot([0,1],[0,1],c='b')
print(type(ax.lines))
print('---------')
for line in ax.lines:
    print(line)
    print('---------')

print(ax.get_xaxis().get_label())
print('---------')
print(ax.get_xaxis().get_label().get_text())
print('---------')
