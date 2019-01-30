#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:15:04 2019

@author: xsxsz
"""

import networkx as nx

G=nx.cubical_graph()
nx.draw(G,pos=nx.circular_layout(G),node_color='g',edge_color='b')
G.clear()
