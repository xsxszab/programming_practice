#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 08:53:11 2019

@author: xsxsz
"""

import json

text="""
{
	"id": 1,
	"number": 234,
	"string": "ebreiu",
	"something":[
	{"a":123},
	{"b":674}
	]
}

"""

file=json.loads(text)
for element in file:
    print(element)
    print(file[element])
    print('---------------')
    
obj={"a":1,"b":2,"c":[1,2,3,4,5,6]}
result=json.dumps(obj)
print(result)
print('---------------')
with open('test.json','w') as file:
    json.dump(obj,file)
