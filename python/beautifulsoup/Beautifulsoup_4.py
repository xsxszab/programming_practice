#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:04:57 2018

@author: xsxsz
"""

import re
import requests
import bs4
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
url='https://www.meishij.net/zuofa/heijiaoyifenchaonongyuheijiaowei.html'
request=requests.get(url,headers=headers)
html=request.text
soup=bs4.BeautifulSoup(html,'lxml')
#print(soup.prettify())
print('-----------------------')
texts=[]
for i in soup.find_all('p'):
    text=i.get_text()
    if text:
        texts.append(text)
print(texts)
print('---------')
