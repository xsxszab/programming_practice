#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:39:54 2018

@author: xsxsz
"""

import argparse

parser=argparse.ArgumentParser(description='This is a parser',epilog='haha')
#print(type(parser))
#print('------------')
#parser.add_argument('echo',help='echo string')
parser.add_argument('--double',help='double the number',type=int)
args=parser.parse_args()
print(args.double*2)
print('------------')
