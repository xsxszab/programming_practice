# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:33:58 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,5))
fig.patch.set_color('g')
fig.canvas.draw()
line=plt.plot([1, 2, 3, 2, 1], lw=4)[0]
line.set(alpha=0.9,zorder=8)
print(fig.patch)