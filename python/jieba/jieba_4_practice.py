#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:31:59 2018

@author: xsxsz
"""

import jieba
string="真是好久好久没来哈皮娜拉野生动物园了，记忆里还是小时候三四年级学校组织春游去的银河系"
print(','.join(jieba.cut(string)))
print('----------')
jieba.suggest_freq(('动物','园'),True)
print(','.join(jieba.cut(string)))
print('----------')
jieba.suggest_freq(('记忆里','还是'),False)
print(','.join(jieba.cut(string)))
print('----------')
