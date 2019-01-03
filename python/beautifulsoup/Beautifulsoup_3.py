#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:33:56 2018

@author: xsxsz
"""

from bs4 import BeautifulSoup
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
soup=BeautifulSoup(html,'lxml')
print(soup.a.next_sibling)
print('-------------')
print(soup.a.next_siblings)
print('-------------')
print(soup.a.previous_sibling)
print('-------------')
print(list(enumerate(soup.a.next_siblings)))
print('-------------')
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup=BeautifulSoup(html,'lxml')
print(type(soup.find(name='ul')))
print('-------------')
print(soup.find(name='ul'))
print('-------------')
print(soup.find(class_='list'))
print('-------------')
