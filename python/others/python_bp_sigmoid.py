#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:06:24 2018

@author: xsxsz
"""

import math

w=[1.0,2.0,-2.0]
x=[2.0,4.0]

dot=w[0]*x[0]+w[1]*x[1]+w[2]
sigmoid=1/(1+math.exp(-dot))

d_sigmoid=sigmoid*(1-sigmoid)
d_x=[w[0]*d_sigmoid,w[1]*d_sigmoid]
d_w=[x[0]*d_sigmoid,x[1]*d_sigmoid,d_sigmoid]
