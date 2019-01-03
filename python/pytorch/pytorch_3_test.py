#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:03:44 2018

@author: xsxsz
"""

import torch

a=torch.randn(2,3)
print(a.data)
print('----------')
print(a.view(1,-1))
print('----------')
print(a.max())
print('----------')
