#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:56:43 2018

@author: xsxsz
"""

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation

fig=plt.figure(0)

ax=fig.add_subplot(111)
line,=ax.plot(np.random.rand(10),c='b')
def update(data):  
    line.set_ydata(data)  
    return line,  
def data_gen():  
    while True:  
        yield np.random.rand(10)  
  
animation=animation.FuncAnimation(fig,update,data_gen,interval=2*1000)  
print(type(animation))
