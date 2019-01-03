# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:21:46 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=np.random.random(200)
y=np.random.random(200)
z=np.random.random(200)
fig=plt.figure()
plt.title('3d')
ax = Axes3D(fig)
plt.scatter(x,y,z)