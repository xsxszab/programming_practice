#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:49:47 2018

@author: xsxsz
"""

import xml.etree.ElementTree as ET
tree=ET.parse('movies.xml')
print(tree)
print('---------')
print(type(tree))
print('---------')
root=tree.getroot()
print(root)
print('---------')
print(root.tag)
print('---------')
print(root.text)
print('---------')
print(root.attrib)
print('---------')
print(root.find('movie'))
print('---------')
node1=root.find('movie')
print(node1.tag)
print('---------')
print(node1.attrib)
print('---------')
print(node1.text)
print('---------')
node2=root.findall('movie')
print(node2)
print('---------')
print(node2[2].tag)
print('---------')
root.remove(node1)
node3=root.findall('moive')
print(node3)
print('---------')
tree.write('movie_processed.xml')
