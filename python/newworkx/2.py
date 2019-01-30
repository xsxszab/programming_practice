#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:22:04 2019

@author: xsxsz
"""

import networkx as nx

G=nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(4,5),(2,4)])
G.add_nodes_from(['abc'])
G.add_cycle(['a','b','c'])
nx.draw(G)
G.clear()
