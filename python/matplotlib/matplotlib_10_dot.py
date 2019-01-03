# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:26:17 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[6,4,3,2,1,3,5]
xn=np.array(x)
yn=np.array(y)
a,b=np.meshgrid(xn,yn)
#plt.xkcd()
print(a)
print('--------------')
print(b)
plt.figure(figsize=(5,5),dpi=80,facecolor='b',edgecolor='r')
plt.grid()
plt.plot(a,b,marker='.',linestyle='',color='g')
