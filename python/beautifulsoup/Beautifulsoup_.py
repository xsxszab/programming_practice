#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 07:09:02 2018

@author: xsxsz
"""

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,'lxml')
find=soup.find('p')
print(type(find))
print('-----------')
print(find)
print('-----------')
print(find.name)
print('-----------')
print(find['class'])
print('-----------')
print(find.string)
print('-----------')
print(soup.head)
print('-----------')
print(soup.tail)
print('-----------')
print(soup.a)
print('-----------')
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup1=BeautifulSoup(markup,'lxml')
print(soup1.b.string)
print('-----------')
print(type(soup1.b.string))
print('-----------')
