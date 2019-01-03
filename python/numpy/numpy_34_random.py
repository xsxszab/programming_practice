#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:58:27 2018

@author: xsxsz
"""

import numpy as np
rand=np.random.RandomState(10)
print(rand.random_sample(size=(2,2)))
print('--------------')
print(rand.randint(10,size=(3,2)))
print('--------------')
print(rand.choice(4,10))
print('--------------')
print(rand.choice(40,10,replace=False))
print('--------------')
