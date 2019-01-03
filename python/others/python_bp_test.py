#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:14:56 2018

@author: xsxsz
"""

import math

x=3.0
y=-4.0

def sigmoid(n):
    return 1/(1+math.exp(-n))

sigy=sigmoid(y)
num = x + sigy
sigx=sigmoid(x)
xpy=x+y
xpysqr=xpy**2
den=sigx+xpysqr
invden=1.0/den
f=num*invden

df_dnum=invden
df_dinvden=num
dinv_dden=-1/(den**2)
dden_dsigx=1
dden_dxpysqr=1
dxpysqr_dxpy=2*xpy
df_dxpy=df_dinvden*dinv_dden*dden_dxpysqr*dxpysqr_dxpy
df_dx=1*df_dxpy
df_dy=1*df_dxpy
df_dx+=(1-sigmoid(x))*sigmoid(x)*dden_dsigx
df_dx+=1*df_dnum
df_dsigy=1*df_dnum
df_dy+=(1-sigmoid(y))*sigmoid(y)*df_dsigy
df_den=df_dinvden*dinv_dden
print(df_dx,df_dy)
print('-----------')
