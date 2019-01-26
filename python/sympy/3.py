#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:09:29 2019

@author: xsxsz
"""

from sympy import *

x=Symbol('x',real=True)
print(expand(exp(I*x),complex=True))
print('---------------------')
temp=series(exp(I*x),x,0,10)
print(temp)