# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:53:40 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-np.pi,np.pi,100)
y=np.sin(x)
plt.figure(figsize=(5,5))
plt.title('$y=\sin x$')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(alpha=0.8)
plt.plot(x,y)
