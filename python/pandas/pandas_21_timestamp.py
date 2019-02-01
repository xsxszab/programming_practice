#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:56:28 2019

@author: xsxsz
"""

from pandas.tslib import Timestamp

current=Timestamp("2018-12-26 17:30:36")
print(current)
print('------------')
current=Timestamp("17:30:36")
print(current)
print('------------')
