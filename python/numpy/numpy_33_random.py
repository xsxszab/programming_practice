#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:40:59 2018

@author: xsxsz
"""

import numpy as np
np.random.RandomState(12)
print(np.random.rand(2,4))
print('--------------')
print(np.random.chisquare(2,10))
print('--------------')
print(np.random.standard_t(2,10))
print('--------------')
print(np.random.standard_cauchy([2,2]))
print('--------------')
