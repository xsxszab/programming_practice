# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:06:32 2019

@author: Administrator
"""

"""
Roman integer
M : 1000
D : 500
C : 100
L : 50
X : 10
V : 5
I : 1
"""

def transform(s):
    ans=0
    projection={'I':1, 'V':5, 'X':10, 'L':50,
                           'C':100, 'D':500, 'M':1000,
                           'IV':4, 'IX':9, 'XL':40, 'XC':90,
                           'CD':400, 'CM':900}
    flag=False
    for i in range(len(s)):
        if flag:
            flag=False
            continue
        if s[i] in projection and s[i:i+2] not in projection:
            ans=ans+projection[s[i]]
            flag=False
        if s[i:i+2] in projection:
            ans=ans+projection[s[i:i+2]]
            flag=True
    return ans

ans=transform('V')
print(ans)
print('---------------')
