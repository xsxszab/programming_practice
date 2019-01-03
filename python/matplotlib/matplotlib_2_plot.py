# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:48:48 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
x=np.linspace(0,20,40)
y1=x**2+1
plt.figure(figsize=(4,4))
plt.plot(x,y1,color='b')
plt.figure()
y2=x**3
plt.plot(x,y2,color='g')
plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlim(0,10)
plt.ylim(0,100)
plt.xlabel('X',fontsize=14)
plt.ylabel('Y',fontsize=14)
plt.xticks(np.linspace(0,10,5))