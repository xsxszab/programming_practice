# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:23:42 2019

@author: Administrator
"""

class Solution():
    def twosum(self,nums,target):
        dic={}
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num],i]
            else:
                dic[target-num]=i
        return 'wrong'

solution=Solution()
ans=solution.twosum([2,7,11,15],9)
print(ans)
print('----------------')
