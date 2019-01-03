#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:57:38 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def sinplot():
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i))

sns.set()
sinplot()
