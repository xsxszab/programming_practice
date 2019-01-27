#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 09:49:17 2019

@author: xsxsz
"""

class message:
    def __init__(self,msg):
        self.msg=msg
    def __repr__(self):
        return 'Message: %s'%self.msg

x=message('hello world')
print(x)