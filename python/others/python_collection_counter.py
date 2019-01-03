#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 07:31:33 2018

@author: xsxsz
"""

import collections
string='sdaghbsiulekjmvlksbhgnemov'
count=collections.Counter(string)
print(count)
print('-------------')
print(count['a'])
print('-------------')
print(count['b'])
print('-------------')
