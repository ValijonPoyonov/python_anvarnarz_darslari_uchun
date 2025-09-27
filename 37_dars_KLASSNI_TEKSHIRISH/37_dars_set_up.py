# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 17:45:06 2025

@author: VALIJON
"""

import unittest
from dars_37_KLASSNI_TEKSHIRISH import Talaba


class Talaba_TEST(unittest.TestCase):
    def setUp(self):
        name='valijon'
        surname='poyonov'
        passport='AB2454545'
        byear=1999
        id_num='F1953612'
        address='djarkurgan'
        self.std3=Talaba(name, surname, passport, byear, id_num)
        self.std4=Talaba(name, surname, passport, byear, id_num,address)
        
    def test_attributes(self):
        self.assertIsNotNone(self.std3.name)
        self.assertIsNotNone(self.std3.surname)
        self.assertIsNotNone(self.std3.passport)
        self.assertIsNotNone(self.std3.byear)
        self.assertIsNotNone(self.std3.id_num)
        self.assertIsNotNone(self.std4.address)
        self.assertEqual('valijon', self.std3.name)
        self.assertEqual('poyonov', self.std4.surname)
        self.assertEqual('djarkurgan', self.std4.address)
        
    def test_get_info(self):
        info="Valijon Poyonov, 1-bosqich talabasi,"
        info+=" 1999-yilda tug'ulgan, ID raqami:F1953612."
        self.assertEqual(info, self.std3.get_info())
        
unittest.main()