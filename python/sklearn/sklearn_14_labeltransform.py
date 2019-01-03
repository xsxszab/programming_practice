#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 10:35:52 2018

@author: xsxsz
"""

from sklearn import preprocessing
list=['a','bbbb','b','a']
lb=preprocessing.LabelBinarizer()
print(lb)
print('----------')
print(type(lb))
print('----------')
print(lb.fit_transform(list))
print('----------')
print(lb.transform(list))
print('----------')
list1=['a','g','a','j','u','r','e','d','d']
print(lb.transform(list1))
print('----------')
print(lb.fit_transform(list1))