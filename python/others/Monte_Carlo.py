#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:49:44 2018

@author: xsxsz
"""

import random
n=1000000
k=0
for i in range(n):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2<=1:
        k+=1

print(4*k/n)