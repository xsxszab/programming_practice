#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:40:44 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
labels=['a','b','c','d']
size=[10,20,30,40]
color=['b','g','r','y']
plt.figure(1,figsize=(10,5))
explode=(0,0.2,0.1,0.05)
plt.pie(size,labels=labels,explode=explode,shadow=True,startangle=0)
plt.axis('equal')