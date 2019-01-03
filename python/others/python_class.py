#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:44:37 2018

@author: xsxsz
"""

class test():
    def __init__(self,name,number):
        self.name=name
        self.number=number
        print('This is init')
    def __del__(self):
        print('delete')
    def print_detail(self):
        print(self.name)
        print('----------------')
        print(self.number)
        print('----------------')

a=test('haha',1234)
a.print_detail()
del(a)
