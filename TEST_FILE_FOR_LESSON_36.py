# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 00:36:54 2025

@author: VALIJON
"""

import unittest
from dars_36_FUNKSIYALARNI_TEKSHIRISH import *

class TEST(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(175,225,311), 311)
    def test_title_it(self):
        listt=['salom','yaxshilik','anvar','salomatlik sirlari']
        def_rsl=title_it(listt)
        self.assertEqual(def_rsl, ['Salom','Yaxshilik','Anvar','Salomatlik Sirlari'])
    def test_in_Fibonachi_False(self):
        self.assertFalse(in_Fibonachi(14))
        self.assertFalse(in_Fibonachi(1500))
        self.assertFalse(in_Fibonachi(64))
        
        
        
        
class Test(unittest.TestCase):
    def test_get_even_number(self):
        self.assertEqual(get_even_number([2,3,55,62,24,42,80,31]), [2,62,24,42,80])
    def test_in_Fibonachi_True(self):
        self.assertTrue(in_Fibonachi(13))
        self.assertTrue(in_Fibonachi(1597))
        self.assertTrue(in_Fibonachi(34))
    

unittest.main()
    
    