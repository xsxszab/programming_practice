#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 22:39:43 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
x=np.linspace(0,20,50)
d=0.5
y=np.sin(x)+d*np.random.randn(50)
plt.title('errorbar')
plt.errorbar(x,y,yerr=d,fmt='.',color='k')
