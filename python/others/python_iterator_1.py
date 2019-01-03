# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 07:31:58 2018

@author: Administrator
"""

class Range(object):
    def __init__(self,n):
        self.idx=0
        self.n=n
    def __iter__(self):
        return self
    def next(self):
        if self.idx<self.n:
            val=self.idx
            self.idx+=1
            return val
        else: 
            raise StopIteration            

a=Range(5)
for i in a:
    print i