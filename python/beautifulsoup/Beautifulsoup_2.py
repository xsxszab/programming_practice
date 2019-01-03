#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:14:48 2018

@author: xsxsz
"""

from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<b href="http://example.com/lacie" class="sister" id="link2">Lacie</b> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())
print('------------')
print(soup.title)
print('------------')
print(soup.title.string)
print('------------')
print(soup.head)
print('------------')
print(soup.p)
print('------------')
print(soup.title.name)
print('------------')
print(soup.p.name)
print('------------')
print(soup.title.attrs)
print('------------')
print(soup.p.attrs)
print('------------')
print(soup.p['name'])
print('------------')
print(soup.head)
print('------------')
print(soup.head.title.string)
print('------------')
print(soup.p.chlidren)
print('------------')
print(soup.head.children)
print('------------')
print(soup.head.contents)
print('------------')
print(soup.title.contents)
print('------------')
print(soup.p.parent)
print('------------')
print(soup.p.parents)
print('------------')
print(list(enumerate(soup.p.parents)))
print('------------')
