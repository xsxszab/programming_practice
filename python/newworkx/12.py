#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:49:27 2019

@author: xsxsz
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()
nx.draw_circular(G, with_labels=True)
