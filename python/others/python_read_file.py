#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:57:26 2018

@author: xsxsz
"""

text=open('test.txt')
print(text)
print('----------')
print(text.read())
print('----------')
print(text.readline())
print('----------')
text1=open('test.txt')
print(text1.readline())
print('----------')
print(text1.readline())
text2=open('test.txt')
print(text2.readlines())
print('----------')
print(text2.readlines())
print('----------')
