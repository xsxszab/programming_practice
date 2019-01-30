#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:36:59 2019

@author: xsxsz
"""

import networkx as nx

G=nx.MultiDiGraph()
G.add_nodes_from([1,2,3])
G.add_weighted_edges_from([(1,2,0.5),(1,2,0.75),(2,3,0.5)])
print(list(G.degree(weight='weight')))
nx.draw(G,with_labels=True)
G.clear()
