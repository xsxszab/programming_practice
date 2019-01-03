# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 09:39:08 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return (1-x/2+x**5+y**3)

num=256
x=np.linspace(-4,4,num)
y=np.linspace(-1,4,num)
a,b=np.meshgrid(x,y)
plt.contourf(a,b,f(a,b),8,alpha=0.75,cmap=plt.cm.hot)
