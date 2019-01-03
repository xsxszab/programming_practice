#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 09:21:05 2018

@author: xsxsz
"""

import torch
import torch.autograd as autograd

x=torch.randn(2,3)
y=torch.randn(2,3)
print(autograd.Variable(x))
print('----------')
print(autograd.Variable(y))
print('----------')
add=x+y
print(autograd.Variable(add))
print('----------')
print(add.data)
print('----------')
print(add.sum())
print('----------')
print(add.backward)
print('----------')
