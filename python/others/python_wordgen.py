#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:50:18 2019

@author: xsxsz
"""

import random

with open('/usr/share/dict/words','r') as file:
    words=file.readlines()

words=[word.rstrip() for word in words]
for word in random.sample(words,5):
    print(word)