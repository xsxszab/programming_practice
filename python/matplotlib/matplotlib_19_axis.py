# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:56:08 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=np.sin(x)
plt.figure()
plt.title('sine')
plt.plot(x,y,color='g',linestyle='--')
plt.xlim(-10,10)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(np.linspace(-10,10,5))
a=plt.gca()
a.spines['right'].set_color('b')
a.xaxis.set_ticks_position('bottom')
a.yaxis.set_ticks_position('left')
a.spines['right'].set_color('none')
a.spines['top'].set_color('none')
a.spines['bottom'].set_position(('data', 0))
a.spines['left'].set_position(('data',0))
plt.show()