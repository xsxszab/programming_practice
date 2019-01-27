#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:14:10 2019

@author: xsxsz
"""

import struct
import string

filename='test.dat'
mask='10s4s4s'
with open(filename,'r') as file:
    for line in file:
        fields=struct.Struct(mask).unpack_from(line)
        print([field.strip() for  field in fields])
