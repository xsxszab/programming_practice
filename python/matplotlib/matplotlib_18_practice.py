# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:41:33 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-20,20,200)
y=1/(1+np.e**(-x))
plt.figure()
plt.plot(x,y)
