#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:52:00 2018

@author: xsxsz
"""

x=-1.0
y=5.0
z=3.0

q=x+y
f=q*z

dfdz=q
dfdq=z
dqdx=1.0
dqdy=1.0

dfdx=dfdq*dqdx
dfdy=dfdq*dqdy

print(dfdx)
print('----------')
print(dfdy)
print('----------')
