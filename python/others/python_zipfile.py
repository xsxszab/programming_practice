#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 07:54:35 2018

@author: xsxsz
"""

import os
import zipfile
z=zipfile.ZipFile('save.zip',mode='w')
if os.path.isdir('zip_test'):
    print('path exists')
    print('-----------')
    for filename in os.listdir('zip_test'):
        z.write('./zip_test/'+filename)
    z.close()