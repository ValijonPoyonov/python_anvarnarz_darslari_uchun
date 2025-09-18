#AMALIYOT
#1-vazifa:
#Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing
# va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
from uuid import uuid4
class Person():
    def __init__(self,name,surname,age,country):
        self.name=name
        self.surname=surname
        self.age=age
        self.country=country
        self.__id=uuid4()
    def get_id(self):
        return self.__id
    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()}, {self.age} years old from {self.country.title()}."
        return info
class Student(Person):
    def __init__(self,name,surname,age,country,direction):
        super().__init__(name, surname, age, country)
        self.direction=direction
        self.__course=1
        self.__status="contract"
    def update_course(self):
        self.__course+=1
        return self.__course
    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()} {self.age} years old "
        info += f"from {self.country.title()}, {self.__course} course student on "
        info+=f"'{self.direction.title()}' direction."
        return info
    def set_status(self,ball):
        if ball>=126.5:
            self.__status="budjet"
        else:
            self.__status="contract"
        return self.__status
alijon=Person("alijon", "poyonov", 28, "O'zbekiston")
valijon=Student("valijon", "poyonov", 26, "O'zbekiston", "mecanics")
#print(alijon.get_info())
#print(alijon.get_id())
#print(valijon.get_id())
#print(valijon.get_info())
#s = valijon.set_status(130)
#print(s)
#k=valijon.update_course()
#print(k)
#print(valijon.get_info())
#print(valijon.get_id())
#print(valijon.__status)

#2-vazifa:
#Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga
# oid xususiyatlar qo'shing.

class Person():
    odamlar_soni = 0
    def __init__(self,name,surname,age,country):
        self.name=name
        self.surname=surname
        self.age=age
        self.country=country
        self.__id=uuid4()
        Person.odamlar_soni+=1
    @classmethod
    def number(cls):
        return Person.odamlar_soni
    def get_id(self):
        return self.__id
    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()}, {self.age} years old from {self.country.title()}."
        return info
class Student(Person):
    talabalar_soni=0
    def __init__(self,name,surname,age,country,direction):
        super().__init__(name, surname, age, country)
        self.direction=direction
        self.__course=1
        self.__status="contract"
        Student.talabalar_soni+=1
    @classmethod
    def count(cls):
        return Student.talabalar_soni
    def update_course(self):
        self.__course+=1
        return self.__course
    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()} {self.age} years old "
        info += f"from {self.country.title()}, {self.__course} course student on "
        info+=f"'{self.direction.title()}' direction."
        return info
    def set_status(self,ball):
        if ball>=126.5:
            self.__status="budjet"
        else:
            self.__status="contract"
        return self.__status
Mahmud=Person("mahmud", "rajabov", 25, "Azarbayjan")
Nigora=Student("nigora", "Xalilova", 35, "tadjikistan", "philosopy")
Smandar=Person("samandar", "ergashev", 21, "turkmaniston")
#print(Person.number())
#print(Student.count())
anvar=Student("anvar", "aliyev", 25, "tadjikistan", "history")
#print(Mahmud.odamlar_soni)

#3-vazifa:
#Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing 