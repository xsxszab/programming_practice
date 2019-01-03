# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:02:42 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
lam=0.4
x=np.arange(0,20,0.1)
plt.xkcd()
plt.figure(frameon=False)
plt.subplot(211)
plt.ylabel('Y')
y=lam*np.exp(-lam*x)
plt.plot(x,y,'bx--')
plt.subplot(212)
plt.xlabel('X')
plt.ylabel('Y')
plt.hist(y,facecolor='g',edgecolor='b',normed=0,alpha=0.8)
