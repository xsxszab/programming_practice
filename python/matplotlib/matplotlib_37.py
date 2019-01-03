#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 22:14:43 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
data=[[1,2,3],[4,5,6],[7,8,9]]
col=['col1','col2','col3']
row=['row1','row2','row3']
plt.table(cellText=data,rowLabels=row,colWidths=[0.1]*3,colLabels=col,loc='best')