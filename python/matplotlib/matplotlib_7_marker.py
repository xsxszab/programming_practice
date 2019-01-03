# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:53:19 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,10,100)
y=np.random.random(100)
plt.figure()
color=np.arctan2(x,y)
plt.title('scatter diagram')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(linestyle='--',linewidth=0.8,axis='x',color='b')
plt.scatter(x,y,s=50,c=color,marker='.')
#plt.scatter(x,y,s=30,c=color,marker=',')
#plt.scatter(x,y,s=30,c=color,marker='.')
#plt.scatter(x,y,s=30,c=color,marker='<')
#plt.scatter(x,y,s=30,c=color,marker='^')
#plt.scatter(x,y,s=30,c=color,marker='2')