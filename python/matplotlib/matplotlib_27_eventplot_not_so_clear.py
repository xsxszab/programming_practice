# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:00:16 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
np.random.seed(200)
data1=np.random.random([6,50])
colors1 = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                    [1, 1, 0],
                    [1, 0, 1],
                    [0, 1, 1]])
lineoffsets1 = np.array([-15, -3, 1, 1.5, 6, 10])
linelengths1 = [5, 2, 1, 1, 3, 1.5]
fig, axs=plt.subplots(2,2)
axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
