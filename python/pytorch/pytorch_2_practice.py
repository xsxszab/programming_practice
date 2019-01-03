#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:00:22 2018

@author: xsxsz
"""

import torch

a=torch.randn(2,3,4)
print(a.numel())
print('--------------')
print(a.size())
print('--------------')
b=torch.squeeze(a,0)
print(b.size())
print('--------------')
c=torch.squeeze(a,1)
print(c.size())
print('--------------')
