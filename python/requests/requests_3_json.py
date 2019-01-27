#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:22:27 2019

@author: xsxsz
"""

import requests

url='https://github.com/timeline.json'
r=requests.get(url)
obj=r.json()
repos=set()
'''
for entry in obj:
    try:
        repos.add(entry['repository']['url'])
    except KeyError as e:
        print('No key %s'%(e))
'''
print('fuck')
