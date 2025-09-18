# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 05:55:27 2025

@author: VALIJON
"""
class Person():
    def __init__(self,name,surname,passport,byear):
        self.name=name
        self.surname=surname
        self.passport=passport
        self.byear=byear
    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()}, {self.byear}-"
        info += f"yilda tug'ilgan, pasport seriyasi: {self.passport.upper()}."
        return info
    def get_age(self,yil):
        return (yil-self.byear)

class Talaba(Person):
    def __init__(self,name,surname,passport,byear,id_num,address):
        super().__init__(name, surname, passport, byear)
        self.id_num=id_num
        self.address=address
        self.course=1
        self.sciences=[]
    def get_info(self):
        """talaba haqida ma'lumot olish"""
        info = f"{self.name.title()} {self.surname.title()}, {self.course}-bosqich talabasi,"
        info += f"{self.byear}-yilda tug'ulgan, ID raqami:{self.id_num.upper()}."
        return info
    def get_id(self):
        """talabani idsini olish"""
        return self.id_num
    def fanga_yozil(self,science):
        """talabaga fan biriktirish"""
        self.sciences.append(science)
        return science.name
    
    def list_sciences(self):
        """talaba obyektiga biriktirilgan fanlar ro'yxati"""
        j=1
        list1=""
        for i in self.sciences:
            list1 += f"{j}) {i.name}\n"
            j+=1
        return list1
    def remove_science(self,science):
        if science in self.sciences:
            self.sciences.remove(science)
        else:
            print("Siz bu fanga yozilmagansiz!\n")
class Address():
    def __init__(self,region,district,street,home_num):
        self.region=region
        self.district=district
        self.street=street
        self.home_num=home_num
    def get_address(self):
        """Obyektning manzilini chop etish"""
        info = f"{self.region.title()} viloyati, {self.district.title()} tumani, "
        info += f"'{self.street.title()}' ko'chasi, {self.home_num}-uy."
        return info
class Sciences():
    def __init__(self,name):
        self.name=name
science1 = Sciences("Matematika")
science2 = Sciences("Tarix")
science3 = Sciences("Iqtisodiyot")
science4 = Sciences("Falsafa")
asadbekmanzil = Address("Navoiy", "Tomchi", "nurafshon", 78)
Asadbek = Talaba("asadbek", "Nurqobilov", "ab2344565", 2003, "id2546361", asadbekmanzil)

science5 = Sciences("Adabiyot")
Asadbek.fanga_yozil(science5)
Valijon = Person('valijon', 'poyonov', 'ab2463533', 1999)
#print(Valijon.get_age(2025))
#print(Valijon.get_info())
alijonmanzil=Address("Surkhandarya", "Djarkurgan", "Qoraqursoq", 73)
Alijon=Talaba("alijon", "poyonov", "aa2453636", 1997, "ID2424", alijonmanzil)
#print(Alijon.get_info())
#print(Alijon.address.home_num)
Alijon.fanga_yozil(science2)
Alijon.fanga_yozil(science3)
Alijon.fanga_yozil(science1)
#print(Alijon.sciences)
#print(science1.name)
print(Asadbek.list_sciences())
print(Alijon.list_sciences())
Alijon.remove_science(science4)
Alijon.remove_science(science3)
print(Alijon.list_sciences())

# 5-vazifa: Person klasidan voris klasslar yaratish.
class User(Person):
    def __init__(self,name,surname,passport,byear,country,phone_number,e_mail):
        super().__init__(name,surname,passport,byear)
        self.country=country
        self.phone_number=phone_number
        self.e_mail=e_mail
    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()} from {self.country.title()}"
        info += f", phone number: {self.phone_number}, e-mail: {self.e_mail}."
        return info
Mavluda = Person("mavluda", "poyonova", "Ab2451565", 2000)
Madina = User("madina", "poyonova","Af1451523",2011, "uzbekistan", "915754818", "poyonovamadinaaa@gmail.com")
print(Mavluda.get_info())
print(Madina.get_info())

class Customer(Person):
    def __init__(self, name, surname, passport, byear,gender,region):
        super().__init__(name,surname,passport,byear)
        self.gender=gender
        self.region=region
        
    def get_info(self):
       info = f"{self.name.title()} {self.surname.title()}, "
       info += f"{self.byear}-year {self.gender} from {self.region.title()}."
       return info
        
Azmat = Customer("azamat", "aliyev", "at4567898", 1996, "male", "Qarshi")
print(Azmat.get_info())







