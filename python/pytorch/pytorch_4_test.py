#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 09:08:45 2018

@author: xsxsz
"""

import torch

a=torch.Tensor([1,2,3])
b=torch.Tensor([4,5,6])
print(torch.cat([a,b],0))
print('----------')
a=torch.randn(2,3)
b=torch.randn(2,3)
print(torch.cat([a,b],0))
print('----------')
print(torch.cat([a,b],1))
print('----------')
a=torch.randn(2,3)
print(a.view(1,6))
print('----------')
a=torch.randn(2,3,4)
print(a.view(2,12))
print('----------')
print(a.view(-1))
print('----------')
