#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:51:44 2018

@author: xsxsz
"""

import os
import re
phone = '18898537584 #这是我的电话号码'
print('我的电话号码:',re.sub('#.*','',phone))
print('-------------')
print(re.sub('\D','',phone))
print('-------------')
ip_addr = re.search('(\d{3}\.){1,3}\d{1,3}\.\d{1,3}',os.popen('ifconfig').read())
print('ip_addr:',ip_addr)
print('-------------')
a = re.match('\d+','2ewrer666dad3123df45')
print(a.group())
print('-------------')
