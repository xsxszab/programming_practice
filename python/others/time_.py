# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:55:02 2018

@author: Administrator
"""

import time
t=time.time()
print "%f"%t
now=time.localtime(t)
print now
time.sleep(3)
i=time.asctime(now)
print i
print time.strftime('%Y-%m-%d %H:%M:%S',now)