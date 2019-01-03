# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:04:59 2018

@author: Administrator
"""

import requests as re
image=re.get('https://cdn.liaoxuefeng.com/cdn/files/attachments/00138676512923004999ceca5614eb2afc5c0efdd2e4640000/0')
print image.url
print'---------'
print image.status_code
print'---------'
image.raise_for_status()
with open('image.png','wb') as f:
    f.write(image.content)