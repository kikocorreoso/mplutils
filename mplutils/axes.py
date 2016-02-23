# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:43:37 2016

@author: kiko
"""
from __future__ import division

def axes_set_better_defaults(ax, axes_color = '#777777', grid = False):
    """
    Enter an Axes instance and it will change the defaults to an opinionated 
    version of how a simple plot should be.
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

# http://matplotlib.org/examples/pylab_examples/spine_placement_demo.html
def axes_set_axis(ax, spines = ['bottom', 'left'], pan = 0):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', pan))  # outward by `pan` points
            spine.set_smart_bounds(True)
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
    
def axes_set_origin(ax, x = 0, y = 0, 
                    xticks_position = 'bottom', yticks_position = 'left',
                    xticks_visible = True, yticks_visible = True):
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
    
def axes_set_aspect_ratio(ax, ratio = 'equal', adjustable = None):
    ax.set_aspect(ratio, adjustable)
