#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 07:41:31 2018

@author: xsxsz
"""

import pdb
def test(arg):
    for i in range(arg):
        print(i)
        print('------------')

arg=4
pdb.run('test(arg)')
