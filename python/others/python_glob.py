#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:25:41 2018

@author: xsxsz
"""

import glob

filenames=glob.glob('*.py')
for filename in filenames:
    print(filename)
    print('-------------')

