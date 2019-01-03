#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 08:25:49 2018

@author: xsxsz
"""


from sklearn.feature_extraction.text import TfidfVectorizer
 
corpus = [
    'This is the first document.',
    'This is the second document.',
    'And the third one',
    'Is this the first document?',
    'I come to American to travel'
]
 
tfidf = TfidfVectorizer().fit_transform(corpus)
print (tfidf)