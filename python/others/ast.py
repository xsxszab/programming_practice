#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:30:06 2019

@author: xsxsz
"""

import ast
tree=ast.dump(ast.parse("(1 + 2) * 3"))
print(tree)