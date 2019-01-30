#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:12:30 2019

@author: xsxsz
"""

import networkx as nx

G=nx.DiGraph()
G.add_nodes_from([1,2,3,4,5,6])
G.add_cycle([1,2,3,4])
G.add_edge(1,3)
G.add_edge(3,1)
nx.draw(G)
G.clear()
