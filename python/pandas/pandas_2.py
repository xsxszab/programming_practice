# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:25:18 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
dict={'a':1,'b':2}
print dict
print'-------------'
s=pd.Series(dict,name='list')
print s
print'-------------'
print s['a']
