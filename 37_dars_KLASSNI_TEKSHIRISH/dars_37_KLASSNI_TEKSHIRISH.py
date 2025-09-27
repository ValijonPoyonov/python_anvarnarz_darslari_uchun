
# 30-darsimizda Shaxs va Talaba klasslarini yaratgan edik.
# Shu ikki klassning xususiyatlari va metodlarini tekshiruvchi test dasturlar yozing. 
# 1-vazifa:
class Person():
    def __init__(self,name,surname,passport,byear):
        self.name=name
        self.surname=surname
        self.passport=passport
        self.byear=byear
    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()}, {self.byear}-"
        info += f"yilda tug'ulgan, pasport seriyasi: {self.passport.upper()}."
        return info
    def get_age(self,yil):
        return (yil-self.byear)

class Talaba(Person):
    def __init__(self,name,surname,passport,byear,id_num,address=''):
        super().__init__(name, surname, passport, byear)
        self.id_num=id_num
        self.address=address
        self.course=1
        self.sciences=[]
    def get_info(self): 
        """talaba haqida ma'lumot olish"""
        info =   f"{self.name.title()} {self.surname.title()}, {self.course}-bosqich talabasi, "
        info += f"{self.byear}-yilda tug'ulgan, ID raqami:{self.id_num.upper()}."
        return info
    def get_id(self):
        """talabani idsini olish"""
        return self.id_num
    def fanga_yozil(self,science):
        """talabaga fan biriktirish"""
        self.sciences.append(science)
        
    
    def list_sciences(self):
        """talaba obyektiga biriktirilgan fanlar ro'yxati"""
        j=1
        list1=""
        for i in self.sciences:
            list1 += f"{j}) {i.title()}\n"
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
manzil_std2=Address('surkhandarya', 'djarkurgan', 'qoraqursoq', 77)
std2=Talaba('alijon', 'poyonov', 'AB1234569', 1997, 'F562314', manzil_std2)
std2.fanga_yozil('mathematics')
std2.fanga_yozil('history')
#print(std2.list_sciences())
#Ikki klass uchun yagona test yoza olasizmi? (isInstance() funksiyasini eslang)