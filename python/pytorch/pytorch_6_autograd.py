#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 09:25:50 2018

@author: xsxsz
"""

import torch as t
from torch.autograd import Variable as V

a=V(t.FloatTensor([2,3]),requires_grad=True)
b=a+3
c=b*b*3
out=c.mean()
out.backward()

print(a.data)
print('-----------')
print(out.data)
print('-----------')
print(a.grad.data)
print('-----------')
