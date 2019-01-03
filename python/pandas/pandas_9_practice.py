#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:14:47 2018

@author: xsxsz
"""

import numpy as np
import pandas as pd
ts = pd.date_range('20000101',periods=300)
cs = pd.DataFrame(np.random.randint(1,10,(300,2)),index = ts)
print(cs)