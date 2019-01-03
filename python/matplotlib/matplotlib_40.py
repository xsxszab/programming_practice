#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:31:16 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
list=[np.random.normal(0, std, 100) for std in range(1, 4)]
plt.figure(figsize=(12,5))
plt.subplot(121)
plt.boxplot(list,notch=True,sym='r')
plt.subplot(122)
plt.violinplot(list,showmedians=True)
