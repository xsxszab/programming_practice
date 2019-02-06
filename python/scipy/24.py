#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:13:05 2019

@author: xsxsz
"""

import numpy as np
from scipy.optimize import minimize

def objective(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2
def constraint1(x):
    return x[0]-2*x[1]+2

def constraint2(x):
    
    return -x[0]-2*x[1]+6

def constraint3(x):
        
    return -x[0]+2*x[1]+2

n=2
x0=np.zeros(n)
x0[0],x0[1]=2,0
b=(0,None)
bounds=(b,b)
con1 = {'type': 'ineq', 'fun': constraint1} 
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3} 
cons = ([con1,con2,con3])

solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bounds,constraints=cons)

print(solution)
print('---------------')
