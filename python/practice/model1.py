# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:56:42 2019

@author: Administrator
"""

#P:利润
#C:折扣

percent=0.15

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def P(C):
    return -(1 + percent*C) * (1500 - C)

x=np.arange(0,1500,100)
plt.plot(x,P(x),color='g')
ans=optimize.minimize(P,200)
plt.scatter(ans.x,P(ans.x),color='b')
print(ans)
print('---------------------')
plt.xlabel('$discount$')
