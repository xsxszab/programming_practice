#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:36:44 2018

@author: xsxsz
"""

import re
import bs4
html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
hahahaha!
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
<b>this is b</b>
</body>
</html>
'''

soup=bs4.BeautifulSoup(html,'lxml')
print(soup.prettify())
print('---------')
taglist=soup.find_all('a')
for tag in taglist:
    print(tag.text)
    print('---------')

print(soup.find_all('a',string=re.compile('Elsie')))
print('---------')

for i in soup.find('body').children:
    if isinstance(i,bs4.element.Tag):
        print(i)
print('---------')
links=[]
for i in soup.find_all('a'):
    link=i.get('href')
    if link:
        links.append(link)
print(links)
print('---------')
for i in soup.find_all('a'):
    string=i.get_text()
    print(string)       