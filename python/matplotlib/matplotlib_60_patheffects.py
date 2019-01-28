#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:54:58 2019

@author: xsxsz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects

data=np.random.randn(10)
fontsize=18
plt.plot(data)
title_obj=plt.title('title')
x_obj=plt.xlabel('X',alpha=0.8)
y_obj=plt.ylabel('Y',alpha=0.8)
title_obj.set_path_effects([patheffects.withSimplePatchShadow()])
offset_xy=(1,-1)
rgbRed=(1.0,0.0,0.0)
pe=patheffects.withSimplePatchShadow(offset=offset_xy,shadow_rgbFace=rgbRed)
x_obj.set_path_effects([pe])
y_obj.set_path_effects([pe])
