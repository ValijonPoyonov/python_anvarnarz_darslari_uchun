# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 22:02:58 2025

@author: VALIJON
"""
from uuid import uuid4

#   32-dars:DUNDER METODLAR
# 1-vazifa:
# Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder
# metodlarni qo'shishni mashq qiling. 
#                1)Obyekt haqida ma'lumot (__rerp__)
#                2)Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)
class Person():
    def __init__(self,name,surname,age,country):
        self.name=name
        self.surname=surname
        self.age=age
        self.country=country
    def __repr__(self):
        return f"{self.name.title()} {self.surname.title()} at {self.age} years old, from {self.country.title()}."
    def __eq__(self,obj):
        return self.age==obj.age
    def __gt__(self,obj):
        return self.age>obj.age
    def __ge__(self,obj):
        return self.age>=obj.age
class Student(Person):
    def __init__(self,name,surname,age,country,course):
        super().__init__(name,surname,age,country)
        self.course=course
        self.id_num = uuid4()
    def get_id(self):
        return self.id_num
    def __str__(self):
        info = f"{self.name.title()} {self.surname.title()} at {self.age} years old"
        info += f", from {self.country.title()}, "
        if self.course==1:
            info += f"{self.course}st course student.id: {self.id_num}"
        elif self.course==2:
            info += f"{self.course}nd course student.id: {self.id_num}"
        else:
            info += f"{self.course}th course student.id: {self.id_num}"
        return info
valijon = Person("valijon", "poyonov", 26, "Uzbekistan")
p2 = Person("jek", "douson", 30, "angliya")
p3 = Person("neymar", "junior", 35, "braziliya")
s1 = Student("aisha", "abdul", 27, "saudia", 2)
s2 = Student("lanesra", "parkinson", 23, "avstraliya", 1)
#print(valijon<p2)

# 2-vazifa:
# Fan degan yangi klass yarating.
# Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin.
# Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__
# kabi metodlarni qo'shing.

#class Science():
#    def __init__(self,name):
#        self.name=name
#        self.students=[]
#    def add_student(self,obj):
#        """adding student to science object"""
#        if isinstance(obj, Student):
#            self.students.append(obj)
#        else:
#            print(f"{type(obj)} is not in Student class.")
#    def __getitem__(self,index):
#        """holding an element of students list by index"""
#        return self.students[index]
#    def __setitem__(self,index,obj):
#        """setting an object to students list by index"""
#        self.students[index]=obj
#        return self.students
#    def __len__(self):
#        """calculation the lenth of students list"""
#        return len(self.students)


# 3-vazifa:
# Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
class Science():
    def __init__(self,name):
        self.name=name
        self.students=[]
    def add_student(self,obj):
        """adding student to science object"""
        if isinstance(obj, Student):
            self.students.append(obj)
        else:
            print(f"{type(obj)} is not in Student class.")
    def __getitem__(self,index):
        """holding an element of students list by index"""
        return self.students[index]
    def __setitem__(self,index,obj):
        """setting an object to students list by index"""
        self.students[index]=obj
        return self.students
    def __len__(self):
        """calculation the lenth of students list"""
        return len(self.students)
    def __sub__(self,obj):
        if isinstance(obj, Student):
            self.students.remove(obj)
        else:
            print(f"{type(obj)} is not in Student class.")
    

    def __add__(self,obj):
        if isinstance(obj,Science):
            new_sc=Science(f"{self.name.title()}-{obj.name.title()}")
            new_sc.students=self.students+obj.students
            
        elif isinstance(obj,Student):
            self.students.append(obj)
        else:
            print(f"{type(obj)} is not in Student class.")
    def __call__(self):
        print(self.students)

sc1=Science("mathematics")
sc2=Science("physics")
sc1.add_student(s1)
sc1.add_student(s2)
s3=Student("mark", "bartra", 24, "spain", 4)
s4=Student("lamine", "yamal", 18, "catalunya", 3)
s5=Student("victor", "luis", 19, "urugvay", 5)
sc2.add_student(s3)
sc2.add_student(s4)
sc2.add_student(s5)
sc2[2]=Student("Arnold", "Aleksandr", 31, "Georgia", 2)
#print(len(sc2))



#print(sc1[:])
s6=Student("Muhammad", "Salah", 39, "egypt", 6)
#print(s6)
s7="sardor"
sc1+s6
#print(sc1.students)
#4-vazifa:
# Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing
# (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)

#sc1+s6
#sc1+s6
#sc1-s6
#sc1-s6
#print(s6)
#print(sc1.students)


# 5-vazifa
# Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)).
# Bu metodlarni o'zingiz istagandek talqin qiling.
sc2()
sc1()