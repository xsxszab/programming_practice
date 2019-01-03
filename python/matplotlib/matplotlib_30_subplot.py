# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:29:49 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
x=np.linspace(-10,10,100)
y=np.sinc(x)
ax1.plot(x,y)
