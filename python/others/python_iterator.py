# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 07:12:58 2018

@author: Administrator
"""

from collections import Iterable
from collections import Iterator
list=[31,72234,34,4,5,6,6,5,4,345]
print isinstance(list,Iterable)
print isinstance(200,Iterable)
print isinstance((x for x in range(10)),Iterable)
print isinstance((x for x in range(10)),Iterator)
print isinstance([],Iterator)
print isinstance(iter([]),Iterator)
