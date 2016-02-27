# -*- coding: utf-8 -*-

"""
Tests for classic module
"""

import unittest
import os

import numpy as np
import matplotlib.pyplot as plt

from mplutils import colors

class colors_mpl_cnames_test(unittest.TestCase):
    
    def test_bad_string(self):
        result = colors.colors_mpl_cnames('kiko') 
        self.assertEqual(repr(result), 
                         'No colors found with kiko in color name')
    
    def test_good_string(self):
        result = colors.colors_mpl_cnames('yellow')
        self.assertEqual(sorted(result.cnames), 
                         ['greenyellow',
                          'lightgoldenrodyellow',
                          'lightyellow',
                          'yellow',
                          'yellowgreen'])
        result = colors.colors_mpl_cnames('maroon')
        self.assertEqual(sorted(result.cnames), 
                         ['maroon'])

class colors_check_grayscale_test(unittest.TestCase):
        
    def test_luminosity_grayscale(self):
        fig, ax = plt.subplots()
        ax.plot([1,2,3], 'b')
        colors.colors_check_grayscale(fig, 
                                      transform = 'luminosity', 
                                      filename = 'temp.png')
        img = plt.imread('temp.png')
        img = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
        self.assertTrue(np.all(img[:,0]*3 == img[:,:3].sum(axis = 1)))
        
    def test_luma_grayscale(self):
        fig, ax = plt.subplots()
        ax.plot([1,2,3], 'b')
        colors.colors_check_grayscale(fig, 
                                      transform = 'luma', 
                                      filename = 'temp.png')
        img = plt.imread('temp.png')
        img = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
        self.assertTrue(np.all(img[:,0]*3 == img[:,:3].sum(axis = 1)))
        
    def test_average_grayscale(self):
        fig, ax = plt.subplots()
        ax.plot([1,2,3], 'b')
        colors.colors_check_grayscale(fig, 
                                      transform = 'average', 
                                      filename = 'temp.png')
        img = plt.imread('temp.png')
        img = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
        self.assertTrue(np.all(img[:,0]*3 == img[:,:3].sum(axis = 1)))
        
    def tearDown(self):
        os.remove('temp.png')
        
if __name__ == "__main__":
    unittest.main(verbosity = 2)