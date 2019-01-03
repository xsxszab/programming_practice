#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:11:02 2018

@author: xsxsz
"""

import jieba
string='如果放到旧字典中将出错。'
print(','.join(jieba.cut(string,HMM=False)))
print('----------')
jieba.suggest_freq(('中','将'),True)
print(','.join(jieba.cut(string,HMM=False)))
print('----------')
