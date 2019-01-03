# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:06:30 2018

@author: Administrator
"""

f=open('sample.txt')
print f.readline()
print'-----------'
print f.readline()
print'-----------'
print f.read()
print'-----------'
f1=open('image.png','rb')
print f1.read()
