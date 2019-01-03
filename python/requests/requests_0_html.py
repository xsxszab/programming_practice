# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:41:14 2018

@author: Administrator
"""

import requests as re
r=re.get('https://baidu.com')
print type(r)
print'-----------'
print r.status_code
print r.text
print'-----------'
print r.content
print'-----------'
print r.content.decode('utf-8')
print'-----------'