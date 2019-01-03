# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:18:55 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,5,0.01)
s=np.exp(-t)
s1=np.sin(t)
s2=np.cosh(0.2*t)
plt.plot()
plt.subplot(211)
plt.plot(t,s,'g')
plt.subplot(212)
plt.plot(t,s1)
plt.plot(t,s2)
