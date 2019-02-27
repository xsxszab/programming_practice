# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:15:32 2019

@author: Administrator
"""

a,b,c=input().strip().split()
a,b,c=int(a),int(b),int(c)
print(a,b,c)
print('----------------')
print(a+b+c,a*b*c,"{:.2f}".format((a+b+c)/3))
print('----------------')
print("{}\n{}\n{:.6f}".format(100,'A',3.14))
print('----------------')
