#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:51:14 2019

@author: xsxsz
"""

import csv
filename='./Nasdaq.csv'
output_filename='./jd.csv'
fread=open(filename,'r')
fwrite=open(output_filename,'w')
ret=csv.writer(fwrite,delimiter=',')
content=fread.readlines()
for line in content[2:]:
    x=line.split(',')
    temp=[]
    j=0
    for t in x:
        if j==0:
            temp.append(t.strip('"'))
        elif j==2:
            temp.append((int(float(t.strip('"')))))
        else:
            temp.append(float(t.strip('"\r\n')))
        j+=1
    ret.writerow(temp)

fread.close()
fwrite.close()
