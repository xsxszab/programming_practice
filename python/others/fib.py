# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:40:45 2018

@author: Administrator
"""

def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    print a
n=input("input:")
fib(n)    