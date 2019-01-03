#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:19:26 2018

@author: xsxsz
"""

import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug('a')
print('----------')
logging.info('b')
logger = logging.getLogger(__name__)    
