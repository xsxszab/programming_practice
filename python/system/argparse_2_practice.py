#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:00:19 2018

@author: xsxsz
"""

import argparse

parser=argparse.ArgumentParser(prog='PROG',usage='%(prog)s [options]')
parser.add_argument('--a',nargs='?',help='This is a')
parser.print_help()
