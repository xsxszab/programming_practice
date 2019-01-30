#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:25:42 2019

@author: xsxsz
"""

import networkx as nx

G=nx.Graph(number=1)
G.add_nodes_from([1,2,3,4])
G.add_weighted_edges_from([(1,2,0.1),(2,3,0.5),(3,4,0.8),(1,3,0.1)])
nx.draw(G,with_labels=True)
print(G.graph)
print('-------------')
G.clear()
