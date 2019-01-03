# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:21:54 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
d=0.2
plt.figure(figsize=(5,5))
x=np.linspace(-10,10,200)
y=np.sinc(x-d)
plt.figure(figsize=(6,5))
plt.axvline(d,linestyle='--',linewidth=2)
plt.plot(x,y,color='g')
plt.annotate('$\delta$',xy=(d+0.4,0.3),color='b',size=20,alpha=0.9)
#plt.title('$\lim_{x\to d}\frac{\sin{x}}{x}  =0$')