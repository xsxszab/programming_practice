# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:44:11 2019

@author: Administrator
"""

def reverse(n):
    ans=''
    if n<0:
        ans=ans+'-'
        n=-n
    numbers=[num for num in str(n)]
    numbers=numbers[::-1]
    for number in numbers:
        ans=ans+number
    return ans

result=reverse(-1234)
print(result)
print('-------------')
