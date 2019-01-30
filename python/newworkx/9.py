#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:34:21 2019

@author: xsxsz
"""

import networkx as nx

G=nx.DiGraph()
G.add_nodes_from([1,2,3])
G.add_weighted_edges_from([(1,2,0.5),(2,3,0.6)])
print(G.out_degree(1,weight='weight'))
print('-------------')
print(list(G.successors(2)))
print('-------------')
