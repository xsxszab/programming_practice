#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:12:27 2019

@author: xsxsz
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

fig=plt.figure()
ax=plt.gca()
#print(type(ax))
start=datetime.datetime(2012,1,5)
end=datetime.datetime(2014,4,7)
delta=datetime.timedelta(days=1)
dates=mpl.dates.drange(start,end,delta)
values=np.random.randn(len(dates))
ax.plot_date(dates,values,color='g',linestyle='-',marker='',label='something')
date_format=mpl.dates.DateFormatter('%y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
fig.legend()