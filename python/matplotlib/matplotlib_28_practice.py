# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:09:19 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
fig=plt.figure(figsize=((5,5)))
ax=fig.add_subplot(111,frameon=False)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_xticks([-0.4,0.3,0.8])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
