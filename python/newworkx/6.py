#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:17:55 2019

@author: xsxsz
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.cycle_graph(20)
pos=nx.spring_layout(G,iterations=200)
nx.draw(G,pos,node_color=range(20),node_size=800,cmap=plt.cm.Blues)
G.clear()
