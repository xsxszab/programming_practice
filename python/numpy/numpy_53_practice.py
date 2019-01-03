#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:16:21 2018

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

mat=np.random.randint(0,100,size=(6,6))

min=np.min(mat)
max=np.max(mat)

ans=(mat-min)/(max-min)

plt.subplot(121)
plt.imshow(mat)
plt.colorbar()
plt.subplot(122)
plt.imshow(ans)
plt.colorbar()
