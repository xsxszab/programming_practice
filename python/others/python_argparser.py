#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:46:53 2018

@author: xsxsz
"""

import argparse
parser=argparse.ArgumentParser()
parser.add_argument('echo')
args=parser.parse_args()
print(args)
print('----------')
print(args.echo)
