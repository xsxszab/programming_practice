#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 09:53:42 2018

@author: xsxsz
"""

import matplotlib.pyplot as plt
plt.figure()
line,=plt.plot([1,2,3],label='label')
plt.legend()
plt.figure()
plt.plot([3,2,1])
plt.legend(['label1'])
plt.figure()
plt.plot([4,5,5,4,4],[8,8,3,3,8])