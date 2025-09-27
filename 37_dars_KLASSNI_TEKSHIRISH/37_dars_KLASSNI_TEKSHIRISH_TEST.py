# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 05:47:25 2025

@author: VALIJON
"""

import unittest
from dars_37_KLASSNI_TEKSHIRISH import Person,Talaba,Address

class PersonTest(unittest.TestCase):
    """classning xususiyatlarini tekshirish"""
    person1=Person('valijon', 'poyonov', 'AB5756817', 1999)
    def test_attributes(self):        
        self.assertIsNotNone(self.person1.name)
        self.assertIsNotNone(self.person1.surname)
        self.assertIsNotNone(self.person1.passport)
        self.assertIsNotNone(self.person1.byear)
        self.assertEqual('valijon', self.person1.name)
        self.assertEqual('poyonov', self.person1.surname)
        self.assertEqual('AB5756817', self.person1.passport)
        self.assertEqual(1999, self.person1.byear)
    def test_get_info(self):        
        person1_info="Valijon Poyonov, 1999-yilda tug'ulgan, pasport seriyasi: AB5756817."
        self.assertEqual(person1_info, self.person1.get_info())
    def test_get_age(self):
        self.assertEqual(26, self.person1.get_age(2025))

class TalabaTest(unittest.TestCase):
    address=Address('surkhandarya', 'djarkurgan', 'qoraqursoq', 73)
    std1=Talaba('valijon', 'poyonov', 'AB5756817', 1999, 'f9999', address)    
    def test_attributes(self):
        self.assertIsNotNone(self.std1.name)
        self.assertIsNotNone(self.std1.surname)
        self.assertIsNotNone(self.std1.passport)
        self.assertIsNotNone(self.std1.byear)
        self.assertIsNotNone(self.std1.id_num)
        self.assertIsNotNone(self.std1.address)
        self.assertIsNotNone(self.std1.course)
        self.assertIsNotNone(self.std1.sciences)
        self.assertEqual('valijon', self.std1.name)
        self.assertEqual('poyonov', self.std1.surname)
        self.assertEqual('AB5756817', self.std1.passport)
        self.assertEqual(1999, self.std1.byear)
        self.assertEqual('f9999', self.std1.id_num)
        self.assertEqual(self.address, self.std1.address)
        self.assertEqual(1, self.std1.course)
    def test_get_info(self):
        info="Valijon Poyonov, 1-bosqich talabasi,"
        info+=" 1999-yilda tug'ulgan, ID raqami:F9999."
        self.assertEqual(info, self.std1.get_info())
    def test_get_id(self):
        self.assertEqual('f9999', self.std1.get_id())
    def test_fanga_yozil(self):
        self.std1.fanga_yozil('mathematics')
        self.std1.fanga_yozil('history')
        self.assertEqual('mathematics', self.std1.sciences[0])
        self.assertEqual('history', self.std1.sciences[1])
        list_sciences="1) Mathematics\n2) History\n"
        self.assertEqual(list_sciences, self.std1.list_sciences())
        
unittest.main()
