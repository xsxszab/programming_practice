# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 07:45:05 2018

@author: Administrator
"""

class Zrange():
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return ZrangeIterator

class ZrangeIterator:
    def __init__(self,n):
        self.i=0;
        self.n=n
    def __iter__(self):
        return self
    def next(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration