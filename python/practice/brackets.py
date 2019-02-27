# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:32:32 2019

@author: Administrator
"""

projection={'}': '{', ']': '[', ')': '(', '>': '<'}
left,right=projection.values(),projection.keys()


def judge(s):
    arr=[]
    for temp in s:
        if temp in left:
            arr.append(temp)
        elif temp in right:
            if arr and arr[-1]==projection[temp]:
                arr.pop()
            else:
                return False
    return True

string1='((([{}])))'
string2='((([{}]))))'
ans1=judge(string1)
print(ans1)
print('-----------------')
ans2=judge(string2)
print(ans2)
print('-----------------')
