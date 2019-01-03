#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:37:04 2018

@author: xsxsz
"""

import csv
filename='data.csv'
with open(filename) as file:
    read=csv.reader(file)
    print(read)
    print('----------')
    print(list(read))
    