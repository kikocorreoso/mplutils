# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:43:37 2016

@author: kiko
"""
from __future__ import division, absolute_import

from .settings import RICH_DISPLAY

import numpy as np
if RICH_DISPLAY:
    from IPython.display import display

def axes_set_better_defaults(ax, 
                             axes_color = '#777777', 
                             grid = False,
                             show = False):
    """
    Enter an Axes instance and it will change the defaults to an opinionated 
    version of how a simple plot should be.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes or matplotlib.axes.Subplot instance
    axes_color : str
        A string indicating a valid matplotlib color.
    grid : bool
        If `True` the grid of the axes will be shown, if `False` (default)
        the grid, if active, will be supressed.
    show : bool
        if `True` the figure will be shown. 
            If you are working in a rich display environment like the IPython 
            qtconsole or the Jupyter notebook it will use 
            `IPython.display.display` to show the figure.
            If you are working otherwise it will call the `show` of the 
            `Figure` instance.
    """
    ax.set_axis_bgcolor((1, 1, 1))
    ax.grid(grid)
    for key in ax.spines.keys():
        if ax.spines[key].get_visible():
            ax.spines[key].set_color(axes_color)
    ax.tick_params(axis = 'x', colors = axes_color)
    ax.tick_params(axis = 'y', colors = axes_color)
    ax.figure.set_facecolor('white')
    ax.figure.canvas.draw()
    if show:
        if RICH_DISPLAY:
            display(ax.figure)
        else:
            ax.figure.show()

# http://matplotlib.org/examples/pylab_examples/spine_placement_demo.html
def axes_set_axis_position(ax, 
                           spines = ['bottom', 'left'], 
                           pan = 0, 
                           show = False):
    """
    Enter an Axes instance and depending the options it will display the
    axis where you selected.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes or matplotlib.axes.Subplot instance
    spines : str or iterable
        A string  or an iterable of strings with the following valid options:
            'bottom' : To active the bottom x-axis.
            'top' : To active the top x-axis.
            'left' : To active the left y-axis.
            'right' : To active the right y-axis.
    pan : int or iterable
        A integer value or an iterable of integer values indicating the value
        to pan the axis. It has to have the same lenght and the same order
        than the spines input.
    show : bool
        if `True` the figure will be shown. 
            If you are working in a rich display environment like the IPython 
            qtconsole or the Jupyter notebook it will use 
            `IPython.display.display` to show the figure.
            If you are working otherwise it will call the `show` of the 
            `Figure` instance.
    """
    if np.isscalar(spines):
        spines = (spines,)
        len_spines = 1
    else:
        len_spines = len(spines)
    if np.isscalar(pan):
        len_pan = 1
    else:
        len_pan = len(pan)
    if len_pan > 1 and len_pan != len_spines:
        raise ValueError(('Length of `spines` and `pan` mismatch. `pan` ')
        ('should be a scalar or should have the same length than `spines`.'))
    
    i = 0
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', pan[i]))  # outward by `pan` points
            spine.set_smart_bounds(True)
            i += 1
        else:
            #spine.set_color('none')  # don't draw spine
            spine.set_visible(False)

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
        ax.tick_params(labelleft = True)
    if 'right' in spines:
        ax.yaxis.set_ticks_position('right')
        ax.tick_params(labelright = True)
    if 'left' in spines and 'right' in spines:
        ax.yaxis.set_ticks_position('both')
        ax.tick_params(labelleft = True, labelright = True)
    if 'left' not in spines and 'right' not in spines:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
        ax.tick_params(labelbottom = True)
    if 'top' in spines:
        ax.xaxis.set_ticks_position('top')
        ax.tick_params(labeltop = True)
    if 'bottom' in spines and 'top' in spines:
        ax.xaxis.set_ticks_position('both')
        ax.tick_params(labelbottom = True, labeltop = True)
    if 'bottom' not in spines and 'top' not in spines:
        ax.xaxis.set_ticks([])
    ax.figure.canvas.draw()
    if show:
        if RICH_DISPLAY:
            display(ax.figure)
        else:
            ax.figure.show()
    
def axes_set_origin(ax, 
                    x = 0, 
                    y = 0, 
                    xticks_position = 'bottom', 
                    yticks_position = 'left',
                    xticks_visible = True, 
                    yticks_visible = True,
                    show = False):
    """
    function to locate x-axis and y-axis on the position you want.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes or matplotlib.axes.Subplot instance
    x : int or float
        Value indicating the position on the y-axis where you want the x-axis
        to be located.
    y : int or float
        Value indicating the position on the x-axis where you want the y-axis
        to be located.
    xticks_position : str
        Default value is 'bottom' if you want the ticks to be located below
        the x-axis. 'top' if you want the ticks to be located above the x-axis.
    yticks_position : str
        Default value is 'left' if you want the ticks to be located on the left
        side of the y-axis. 'right' if you want the ticks to be located on the
        right side of the y-axis.
    xticks_visible : bool
        Default value is True if you want ticks visible on the x-axis. False 
        if you don't want to see the ticks on the x-axis.
    yticks_visible : bool
        Default value is True if you want ticks visible on the y-axis. False 
        if you don't want to see the ticks on the y-axis.
    show : bool
        if `True` the figure will be shown. 
            If you are working in a rich display environment like the IPython 
            qtconsole or the Jupyter notebook it will use 
            `IPython.display.display` to show the figure.
            If you are working otherwise it will call the `show` of the 
            `Figure` instance.
    """
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position(xticks_position)
    ax.spines['bottom'].set_position(('data', x))
    ax.yaxis.set_ticks_position(yticks_position)
    ax.spines['left'].set_position(('data', y))
    if not xticks_visible:
        ax.set_xticks([])
    if not yticks_visible:
        ax.set_yticks([])
    ax.figure.canvas.draw()
    if show:
        if RICH_DISPLAY:
            display(ax.figure)
        else:
            ax.figure.show()
    
def axes_set_aspect_ratio(ax, ratio = 'equal', show = True):
    """
    function that accepts an Axes instance and update the information
    setting the aspect ratio of the axis to the defined quantity
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes or matplotlib.axes.Subplot instance
    ratio : str or int/float
        The value can be a string with the following values:
            'equal' : (default) same scaling from data to plot units for x and y
            'auto' : automatic; fill position rectangle with data
        Or a:
            number (int or float) : a circle will be stretched such that the 
            height is num times the width. aspec t =1 is the same as
            aspect='equal'.
    show : bool
        if `True` the figure will be shown. 
            If you are working in a rich display environment like the IPython 
            qtconsole or the Jupyter notebook it will use 
            `IPython.display.display` to show the figure.
            If you are working otherwise it will call the `show` of the 
            `Figure` instance.
    """
    ax.set_aspect(ratio, adjustable = None)
    if show:
        if RICH_DISPLAY:
            display(ax.figure)
        else:
            ax.figure.show()