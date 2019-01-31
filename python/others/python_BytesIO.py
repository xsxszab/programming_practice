#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:46:20 2019

@author: xsxsz
"""

from io import BytesIO

f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print('------------')
f.close()
