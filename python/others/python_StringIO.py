#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:39:08 2019

@author: xsxsz
"""

from io import StringIO

f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
print('---------')
f.close()
