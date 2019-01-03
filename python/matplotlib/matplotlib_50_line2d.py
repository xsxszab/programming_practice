#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 07:49:38 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
fig=plt.figure(0)
line1=plt.Line2D([0,1],[0,1],transform=fig.transFigure,figure=fig,c='g')
line2=plt.Line2D([0,1],[1,0],transform=fig.transFigure,figure=fig,c='b')
fig.lines.extend([line1,line2])
