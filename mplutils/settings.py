# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:35:00 2016

@author: x003621
"""

try:
    get_ipython().kernel
except:
    RICH_DISPLAY = False
else:
    RICH_DISPLAY = True