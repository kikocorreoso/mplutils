# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:17:28 2016

@author: kiko
"""

import string
import os
import random

import matplotlib as mpl
import matplotlib.pyplot as plt

class colors_mpl_cnames:
    """
    Helper class to know the available color names in Matplotlib. The result
    is a string with the name aliases and the HTML code. If used in a Jupyter
    notebook the result will be a HTML table with the name, code and a cell
    with the color.
    
    Parameters
    ----------
    color : str
        `color` is a string indicating a color. If defined, the result will
        be all the colors having `color` in the matplotlib color name aliases. 
        If not defined the result is a string with the list of all 
        available color name aliases.
    """
    def __init__(self, color = None):
        self.color = color
        if self.color:
            self.cnames = {}
            for key, value in mpl.colors.cnames.items():
                if self.color in key:
                    self.cnames[key] = value
        else:
            self.cnames = mpl.colors.cnames
        
        
    def __repr__(self):
        if self.color and len(self.cnames) == 0:
            return "No colors found with {} in color name". format(self.color)
        out = ""
        for key, value in self.cnames.items():
            out += '{}:{}\n'.format(key, value)
        return out
    
    def _repr_html_(self):
        if self.color and len(self.cnames) == 0:
            return "No colors found with {} in color name". format(self.color)
        html = "<table>\n"
        for key, value in self.cnames.items():
            html += "  <tr>\n"
            html += "    <td>" + key + "</td>\n"
            html += "    <td>" + value + "</td>\n"
            html += '    <td bgcolor="' + value + '" width="50px"></td>\n'
        html += "</table>"
        return html

def colors_check_grayscale(fig, transform = 'luminosity', filename = None):
    tmp = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    tmp = tmp + '.png'
    fig.savefig(tmp)
    hgt = fig.get_figheight()
    wdt = fig.get_figwidth()
    dpi = fig.get_dpi()
    im  = plt.imread(tmp)
    #im = np.asarray(im)
    im = im[..., 0:3]
    # https://en.wikipedia.org/wiki/Grayscale#Colorimetric_.28luminance-preserving.29_conversion_to_grayscale
    if transform == 'luminosity': 
        data = im[:,:,0] * 0.2126 + im[:,:,1] * 0.7152 + im[:,:,2] * 0.0722
        #data = np.average(im, -1, weights=[.2126, .7152, 0.0722])
    # https://en.wikipedia.org/wiki/Grayscale#Luma_coding_in_video_systems
    elif transform == 'luma': 
        data = im[:,:,0] * 0.299 + im[:,:,1] * 0.587 + im[:,:,2] * 0.114
        #data = np.average(im, -1, weights=[.2126, .7152, 0.0722])
    elif transform == 'average':
        data = (im[:,:,0] + im[:,:,1] + im[:,:,2]) / 3
        #data = np.average(im, -1)
    else:
        raise print('transform value supplied not valid')
    fig1 = plt.figure(figsize = (wdt, hgt), dpi = dpi)
    ax = fig1.add_axes([0,0,1,1])
    ax.imshow(data, vmin = 0, vmax = 1, cmap = plt.get_cmap('Greys_r'))
    ax.axis('off')
    if filename:
        fig1.savefig(filename, dpi = dpi)
    os.remove(tmp)