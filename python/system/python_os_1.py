#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:05:53 2018

@author: xsxsz
"""

import os
print(os.getcwd())
print('---------')
print(os.listdir())
print('---------')
print(os.path.abspath('.'))
print('---------')
print(os.path.abspath('..'))
print('---------')
print(os.path.split('.'))
print('---------')
print(os.path.split('/resource/repository_python/python/python_os_1.py'))
print('---------')
print(os.path.join('/path','name.py'))
print('---------')
print(os.path.dirname('/resource/repository_python/python/python_os_1.py'))
print('---------')
print(os.path.basename('/resource/repository_python/python/python_os_1.py'))
print('---------')
print(os.path.getatime('/resource'))
print('---------')
print(os.path.getatime('/resource'))
print('---------')
print(os.path.getctime('/resource'))
print('---------')
print(os.path.getsize('python_os_1.py'))
print('---------')
print(os.path.exists('python_os_1.py'))
print('---------')
print(os.sep,os.extsep,os.pathsep,os.linesep)
print('---------')
