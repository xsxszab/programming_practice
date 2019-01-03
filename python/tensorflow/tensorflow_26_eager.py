#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:48:51 2018

@author: xsxsz
"""

import numpy as np
import tensorflow as tf
import tensorflow.contrib.eager as tfe

tfe.enable_eager_execution()
a=tf.constant(2)
b=tf.constant(3)
c=a+b
d=a*b

print('a=%i'%a)
print('-----------')
print('b=%i'%b)
print('-----------')
print('c=%i'%c)
print('-----------')
print('d=%i'%d)
print('-----------')
