#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:21:30 2019

@author: xsxsz
"""

from sympy import *

x=Symbol('x')
print(integrate(sin(x)))
print('----------------')
print(integrate(x*sin(x)))
print('----------------')
print(integrate(x*sin(x), (x, 0, 2*pi)))