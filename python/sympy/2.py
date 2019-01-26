#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:18:03 2018

@author: xsxsz
"""
import sympy as sy
import matplotlib.pyplot as  plt
sy.init_session(use_latex=True)
sy.init_printing(use_latex=True)
print sy.sqrt(8)
x=sy.symbols('x')
print'--------'
print x
print'--------'
y=sy.Function('y')
y1=2*x
print y1
print'--------'
y2=sy.diff(x*2)
print y2
print'--------'
y3=sy.diff(sy.exp(x)*sy.sin(x))
print y3
print'--------'
print sy.latex(y3)
print'--------'
