#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:17:09 2019

@author: xsxsz
"""

import networkx as nx

G=nx.path_graph(10)
nx.draw(G)
G.clear()
