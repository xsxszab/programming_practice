#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 09:26:33 2018

@author: xsxsz
"""

import pandas as pd
left=pd.DataFrame({'key1':['K0','K0','K1','K2'],
                             'key2':['K0','K1','K0','K1'],
                             'A':['A0','A1','A2','A3'],
                             'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                              'key2':['K0','K0','K0','K0'],
                              'C':['C0','C1','C2','C3'],
                              'D':['D0','D1','D2','D3']})
print(left)
print('-------------')
print(right)
print('-------------')
print(pd.merge(left,right))
print('-------------')
print(pd.merge(left,right,on='key1'))
print('-------------')
print(pd.merge(left,right,on='key2'))
print('-------------')
print(pd.merge(left,right,how='left'))
print('-------------')
