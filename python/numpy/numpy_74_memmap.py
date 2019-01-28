#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:15:28 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt

filename='chair.jpg'
image=np.memmap(filename,dtype=np.uint8,shape=(420,420))
plt.imshow(image)
plt.colorbar()