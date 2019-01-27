#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:29:51 2019

@author: xsxsz
"""

import xlrd

filename='test.xlsx'
wb=xlrd.open_workbook(filename)
ws=wb.sheet_by_name('Sheet1')
data=[]
for r in range(ws.nrows):
    col=[]
    for c in range(ws.ncols):
        col.append(ws.cell(r,c).value)
    data.append(col)
    
print(data)
print('--------------')
