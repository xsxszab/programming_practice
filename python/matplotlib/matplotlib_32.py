#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:15:20 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,10,100)
y=x**(1/x)
plt.figure(figsize=(6,5))
plt.plot(x,y)
plt.title('Fuck')