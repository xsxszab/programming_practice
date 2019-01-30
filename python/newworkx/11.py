#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:40:50 2019

@author: xsxsz
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.balanced_tree(3, 5)
plt.figure(figsize=(8,8))
nx.draw(G,node_size=20, alpha=0.5, node_color="blue", with_labels=False)
