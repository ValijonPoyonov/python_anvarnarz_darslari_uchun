class Avto():
    def __init__(self,make,model,narh,rang,yil):
        self.make=make
        self.model=model
        self.narh=narh
        self.rang=rang
        self.yil=yil
    def __repr__(self):
        """Oynaga tushunarliroq malumot chiqarish"""
        return f"{self.make.title()} {self.rang} '{self.model.title()}' {self.yil}-yil, {self.narh} dollar."
    def __eq__(self, obj2):
        """Ikkita obyektning ma'lum bir hususiyatlarini tengligini tekshiruvchi metod"""
        return self.narh==obj2.narh
    def __lt__(self,obj2):
        """Ikkita obyektning biri ikkinchisidan kichikmi yoki yo'qmi ekanligini tekshiradi"""
        return self.narh<obj2.narh
    def __le__(self,obj2):
        """Ikkita obyektning biri ikkinchisidan kichik yoki tengligini tekshiradi"""
        return self.narh<=obj2.narh
avto2=Avto("GM", "jentra", "12000", "oq", 2020)
avto1=Avto("BMW", "X5", "55000", "qora", 2025)
#print(avto1)
#repr(avto1)
#str(avto1)
#print(avto1.__eq__(avto2))
#print(avto2.__lt__(avto1))
#print(avto1.__le__(avto2))
#print(avto1!=avto2)

class AvtoSalon():
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
    def __str__(self):
        """Shu klasdan yaratilgan obyekt haqida tushunarli ma'lumot chop etish."""
        return f"{self.name.title()} avtosaloni."
    def add_avto(self,*avtolar):
        """AvtoSalon obyektiga Avto obyektini qo'shish"""
        for avto in avtolar:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print(f"{avto} Avto klasiga tegishli emas.")
        
    def show_avtolar(self):
        """AvtoSalon obyektida mavjud bo'lgan obyektlarni tartib bilan chop etish"""
        j=1
        for i in self.avtolar:
            print(f"{j}) {i}")
            j+=1
    def __len__(self):
        """obyekt uzunligini aniqlash"""
        #print(f"Hozirda {self.name.title()} avtosalonida {len(self.avtolar)} ta avtomobil bor.")
        return len(self.avtolar)
    def __getitem__(self,index):
        """obyektga index orqali murojat qilish"""
        print(self.avtolar[index])
    def __setitem__(self,index,value):
        """obyektning ma'lum indexdagi elementini o'zgartirish"""
        if isinstance(value,Avto):
            self.avtolar[index]=value
        else:
            print("Kiritilgan obyekt Avto klasiga tegishli emas.")
    def __add__(self,value):
        """Classning ikkita obyektini qo'shish"""
        if isinstance(value, AvtoSalon):
            new_salon=AvtoSalon(f"{self.name.title()} --- {value.name.title()}")
            new_salon.avtolar=self.avtolar+value.avtolar
            return new_salon
        else:
            print("Kiritilgan qiymat AvtoSalonga tegishli emas.")
    def __call__(self):
        """obyektni metod kabi funksiya kambi chaqirish"""
        print([avto for avto in self.avtolar])
zargarlik=AvtoSalon("zargarlik")
#print(zargarlik)
avto3=Avto("GM", "Neksiya",8000 ,"oq", 1999)
avto4=Avto("Lexsus", "niva", 36000, "silver", 2003)
zargarlik.add_avto(avto1)
zargarlik.add_avto(avto2)
zargarlik.add_avto(avto3)
zargarlik.add_avto(avto4)
avto5="neksiya"
#zargarlik.add_avto(avto5)
#print(zargarlik.avtolar)
#zargarlik.show_avtolar()
#print(len(zargarlik))
#print(zargarlik[0])
#print(zargarlik[1])
#print(zargarlik[2])
#print(zargarlik[3])
#print(zargarlik[:])

avto6=Avto("daewo", "tico", 3000, "yashil", 1990)
#print(zargarlik[3])
#zargarlik[3]=avto6
#print(zargarlik[3])
#zargarlik.show_avtolar()
yakkasaroy=AvtoSalon("yakkasaroy")
avto7=Avto("Nissan", "gtr5", 70000, "qizil", 2024)
avto8=Avto("Audi", "sls130", 65000, "sariq", 2023)
yakkasaroy.add_avto(avto6)
yakkasaroy.add_avto(avto7)
yakkasaroy.add_avto(avto8)
#zargarlik.show_avtolar()
#yakkasaroy.show_avtolar()
zargarlik()