#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:57:17 2018

@author: xsxsz
"""

from bs4 import BeautifulSoup
html_str = """
        <ul>
            <li>
                <a href="http://www.baidu.com/">findfind</a>
            </li>
            <li>sadklfoilbneroiskhbvjaoiksbneoifalgrkebsjjjjjjjjjjjj</li>
            <li>
                <a class="baidu" href="http://www.baidu.com/">nothing</a>
                <a class="bi" href="http://www.baidu.com/">nogsadtghibrrhrng</a>

            </li>
            <li>
                <a  id="lagou" href="http://www.lagou.com/">lagou</a>
            </li>
            <li>
                <label class="enterText enterArea">hahahahaha：</label>
                <p class="enterImg">
                    <img id="previewImage" title='mmm' src="http://www.google.com/logo.png"/>
                </p>
                <div class="Validform_checktip">ghershrsagsehtjyrj</div>
            </li>
        </ul>
    """
soup=BeautifulSoup(html_str,'lxml')
print(soup)
print('-----------')
print(type(soup))
print('-----------')
print(soup.text)
print('-----------')
print(soup.find('a'))
print('-----------')
print(soup.find('a').text)
print('-----------')
print(soup.find('a',class_='bi'))
print('-----------')
print(soup.find('a',class_='bi').text)
print('-----------')
print(soup.find_all('a'))
print('-----------')
print(soup.find_all('li'))
print('-----------')
print(soup.prettify)
print('-----------')
print(soup.contents)
print('-----------')
print(soup.head)
print('-----------')
print(soup.prettify())
print('-----------')
