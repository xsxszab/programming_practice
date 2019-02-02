#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:23:06 2019

@author: xsxsz
"""

import socket

myHost=''
myPort=50007
socketobj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketobj.bind((myHost,myPort))
socketobj.listen(5)
while True:
    connection,address=socketobj.accept()
    print('Sever connected by',address)
    while True:
        data=connection.recv(1024)
        if not data:
            break
        connection.send('message from sever:',data)
    connection.close()
