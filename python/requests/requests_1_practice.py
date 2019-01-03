# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:53:57 2018

@author: Administrator
"""

import requests as re

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
response =re.get("https://www.zhihu.com",headers=headers)
print response.text
print'------------'
print response.status_code
print'------------'
print response.url
print'------------'
print response.history
print'------------'
print response.cookies
print'------------'
print response.headers
print'------------'
print response.status_code==re.codes.ok