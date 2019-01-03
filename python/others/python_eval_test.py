# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:06:00 2018

@author: Administrator
"""

x=1
y=1
num1=eval('x+y')
print(num1)

def g():
    x,y=2,2
    num3=eval('x+y')
    print(num3)
    num2=eval('x+y',globals())
    print(num2)
    num4=eval('x+y',locals())
    print(num4)

print('---------')
g()