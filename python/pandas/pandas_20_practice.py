#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:50:10 2019

@author: xsxsz
"""

import numpy as np
import pandas as pd

data=np.random.randn(200, 3)
ind=pd.date_range('2018-12-25', periods = 200)
df=pd.DataFrame(data, index=ind, columns=["A", "B", "C"])
dfc=df.cumsum()
dfc["A"].hist(normed = True)
dfc["A"].plot(kind = "kde")
dfc["B"].hist(normed = True)
dfc["B"].plot(kind = "kde")
dfc["C"].hist(normed = True)
dfc["C"].plot(kind = "kde")
