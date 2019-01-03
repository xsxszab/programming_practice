#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 10:43:44 2018

@author: xsxsz
"""

import  jieba
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print('----------')
jieba.suggest_freq(('中', '将'), True)
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print('----------')
