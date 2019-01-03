# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:51:10 2018

@author: Administrator
"""

import pandas as pd
list=[1,2,32,4,2,3,4,2,2,44]
dict={'a':[23,5],'b':[765,3],'c':[23,1]}
frame=pd.DataFrame(list)
print frame
print'----------'
frame1=pd.DataFrame(dict)
print frame1
print'----------'
order=['one','two',]
frame2=pd.DataFrame(dict,index=order)
print frame2
print'----------'
print frame2['a']
print'----------'
print frame2['a']['one']
print'----------'
print frame2['a'][1]
print'----------'
frame2['i']=10
print frame2
print'----------'
frame2['i']=5
print frame2
print'----------'
frame2['i'][1]=10
print frame2
print'----------'
judge=(frame2.i==10)
print judge
frame2['i']=judge
print frame2
print'----------'
print frame.sort_index()
print'----------'
print frame.sort_index(ascending=False)
print'----------'
print frame2.sort_values(by=['a'])
print'----------'
print frame2.rank()
print'----------'
print frame2.rank(axis=1)
print'----------'
