#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 07:12:10 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig=plt.figure(1)
gs=GridSpec(3,3)

ax1=plt.subplot(gs[0,:])
ax2=plt.subplot(gs[1,:2])
ax3=plt.subplot(gs[1:,2])
ax4=plt.subplot(gs[2,:2])
