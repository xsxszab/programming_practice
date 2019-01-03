#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:10:18 2018

@author: xsxsz
"""

import re

string1='agerewrehjjjjjjjjjage1294783584395349y82558hjjjjjjjjjjjjjjjjjjjj'

def find(p,string):
    pattern=re.compile(p)
    print(pattern.findall(string))
    print('-------------')

find('hj{9,}',string1)
find('hj{10,}',string1)
find('hj{2,10}',string1)
find('^a',string1)
find('j$',string1)
find('[0-9]+',string1)
find('[0-9a-z]+',string1)
find('',string1)
find('hj{2,}?',string1)
find('age(?=1)',string1)
