#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 20:24:01 2019

@author: xsxsz
"""

import itchat
import time

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print('messege received:',msg.text)
itchat.auto_login()
time.sleep(5)
itchat.send('to filehelper',toUserName='filehelper')
itchat.run()









print('fuck')
