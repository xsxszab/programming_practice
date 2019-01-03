#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 07:21:04 2018

@author: xsxsz
"""

import jieba
import jieba.posseg as psg

jieba.enable_parallel(4)

string='我去北京故宫博物院参观'
cut=jieba.cut(string)
print(cut)
print('---------------')
print(','.join(cut))
print('---------------')
print(','.join(jieba.cut(string,cut_all=True)))
print('---------------')
print(','.join(jieba.cut_for_search(string)))
print('---------------')
print(','.join(jieba.cut_for_search(string,HMM=True)))
print('---------------')
print([(x.word,x.flag) for x in psg.cut(string)])
print('---------------')
print(jieba.lcut(string))
print('-------------')
