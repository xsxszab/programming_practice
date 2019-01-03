#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:42:30 2018

@author: xsxsz
"""

import sympy as sy
sy.init_printing(use_unicode=True,use_latex=True)
x,y=sy.symbols('x y')
expr=x+y**2
latex=sy.latex(expr)
print(latex)
print('----------')
print(sy.solve(x+1,x))
print('----------')
print(sy.limit(sy.sin(x)/x,x,0))
print('----------')
print(sy.limit(sy.sin(x)/x,x,sy.oo))
print('----------')
print(sy.limit(sy.ln(x+1)/x,x,0))
print('----------')
print(sy.integrate(sy.sin(x),(x,-sy.oo,sy.oo)))
print('----------')
print(sy.integrate(1/x,(x,1,2)))
print('----------')
print(sy.Rational(1,2))
print('----------')
