# -*- coding: utf-8 -*-
"""
Text utilities to be used 

@author: x003621
"""
from __future__ import division

import matplotlib as mpl

def text_getinfo_availablesystemfonts():
    return mpl.font_manager.findSystemFonts(fontpaths=None)

#def text_set_properties(family = 'sans-serif', style = 'normal',
#                        variant = 'normal', stretch = 'normal',
#                        weight = 'normal', size = 'medium'):
#    """
#    This is just a convenient wrapper around 
#    `matplotlib.font_manager.FontProperties` including easier font sizes
#    definitions.
#    
#    The way to use it is similar to `matplotlib.font_manager.FontProperties`
#    except you can define the `size` property using one of the following
#    shortcuts:
#    
#        'xxs': 'xx-small', 
#        'xs': 'x-small',
#        's': 'small', 
#        'm': 'medium', 
#        'l': 'large', 
#        'xl': 'x-large', 
#        'xxl': 'xx-large'
#    
#    For more info use `help(matplotlib.font_manager.FontProperties)`.
#    """
#    _sizes = {
#        'xxs': 'xx-small', 
#        'xs': 'x-small',
#        's': 'small', 
#        'm': 'medium', 
#        'l': 'large', 
#        'xl': 'x-large', 
#        'xxl': 'xx-large'
#	}
#    if size in ['xxs', 'xs', 's', 'm', 'l', 'xl', 'xxl']:
#        size = _sizes[size]
#    fm = mpl.font_manager.FontProperties(family, style, variant, stretch,
#                                         weight, size)
#    return fm
