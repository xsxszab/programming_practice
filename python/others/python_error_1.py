#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:26:54 2018

@author: xsxsz
"""

import sys
a=2
b=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print('error')

try:
    f = open('data.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print(err)
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
