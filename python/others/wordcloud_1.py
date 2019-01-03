#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 18:49:22 2018

@author: xsxsz
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

string="the answer to life the universe and everything--42."
word=WordCloud(background_color='white',width=1000,height=800).generate(string)
plt.imshow(word)
plt.axis('off')