#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 20:29:25 2019

@author: xsxsz
"""

import pandas as pd
import tushare as ts

df=ts.realtime_boxoffice()
print(df)
print('--------------')
df=ts.get_cpi()
print(df)
print('--------------')
df=ts.get_stock_basics()
print(df)
print('--------------')
df.to_csv('./stock.csv')
