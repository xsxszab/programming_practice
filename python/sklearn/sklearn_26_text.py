#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 08:06:25 2018

@author: xsxsz
"""
from sklearn.feature_extraction.text import CountVectorizer
text = ["The quick brown fox jumped over the lazy dog."]
count=CountVectorizer(encoding='utf-8',min_df=1)
count.fit(text)
print(count.vocabulary_)
print('-------------')
vector=count.fit_transform(text)
print(vector)
print('-------------')
print(type(vector))
print('-------------')
print(vector.toarray())
print('-------------')
print(vector.shape)
print('-------------')
