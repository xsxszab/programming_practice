# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:57:39 2019

@author: Administrator
"""

def judge(n):
    length=len(str(n))
    string=str(n)
    i,j=0,length-1
    while i<=j:
        if string[i]!=string[j]:
            return False
        i,j=i+1,j-1
    return True
    

ans=judge(1234321)
print(ans)
print('---------------')
