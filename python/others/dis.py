#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:37:27 2019

@author: xsxsz
"""

import dis

def hello():
    print("hello world!")

dis.dis(hello)
print('-------------------')
print(hello.__code__)