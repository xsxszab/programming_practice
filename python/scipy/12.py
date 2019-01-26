#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:31:39 2019

@author: xsxsz
"""

import numpy as np
from scipy import integrate

def f(x,y):
    return x*y
def h(x):
    return x
value,err=integrate.dblquad(f, 1, 2, lambda x: 1, h)
print(value)