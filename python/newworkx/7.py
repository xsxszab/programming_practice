#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:20:48 2019

@author: xsxsz
"""

import networkx as nx

G=nx.petersen_graph()
nx.draw(G,with_labels=True,font_weight='bold')
G.clear()
