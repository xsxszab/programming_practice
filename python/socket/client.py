#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:33:24 2019

@author: xsxsz
"""

import socket

serverHost = 'localhost'
serverPort = 50007
message=['hello world!']
socketobj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketobj.connect((serverHost,serverPort))
for line in message:
    socketobj.send(line)
    data=socketobj.recv(1024)
    print('received:',repr(data))
socketobj.close()
