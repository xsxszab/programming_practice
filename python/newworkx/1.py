#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:14:48 2019

@author: xsxsz
"""

import networkx as nx

G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_edge(1,2)
e=(2,3)
G.add_edge(*e)
print(G.number_of_nodes())
print('---------------')
print(G.number_of_edges())
print('---------------')
print(G.nodes)
print('---------------')
print(G.edges)
print('---------------')
print(G.degree[1])
print('---------------')
print(G.degree([2,3]))
G.remove_edge(2,3)
G.remove_node(3)
print(G.number_of_nodes())
print('---------------')
print(G.number_of_edges())
print('---------------')
G.clear()
