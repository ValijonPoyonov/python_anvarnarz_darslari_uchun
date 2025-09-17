class Avto():
    """Avtomobillar yaratish uchun shablon"""
    def __init__(self,company,model,year,colour,price):
        self.company=company
        self.model=model
        self.year=year
        self.colour=colour
        self.price=price
        self.kilometres=0
        self.sell_time=1
    def get_info(self):
        """Obyekt haqidagi ma'lumotlarni qaytaradi"""
        info = f"{self.company.title()}, {self.model.title()} {self.year}-yil, "
        info += f"rangi {self.colour}, narxi {self.price},"
        info += f" {self.sell_time}-qo'l, {self.kilometres} km yurgan."
        return info
    def set_kilometres(self,km):
        self.kilometres=km
    def update_sell_time(self):
        self.sell_time+=1
    
class Avtosalon():
    def __init__(self,name,location,contact):
        self.name=name
        self.location=location
        self.contact=contact
        self.cars=[]
        self.amount_cars=0
    def add_car(self,car):
        """Obyektga obyektlar biriktirish, avtosalonga avtomobillar qo'shish."""
        self.cars.append(car)
        self.amount_cars+=1
    def delete_car(self,car):
        self.cars.remove(car)
        self.amount_cars-=1
    def show_cars(self):
        """Avtosalondagi mavjud avtomobillarni namoyish qiluvchi metod"""
        return [car.get_info() for car in self.cars]
avto1=Avto("General Motors", "Nexia", 2002, "oq", 9000)
avto1.set_kilometres(7500)
avto1.update_sell_time()
avto2=Avto("BMW", "X5", 2023, "qora", 75000)
avto3=Avto("build your dreams", "Chazor",2025,"silver",45000)
info = avto3.get_info()
Avtosalon1 = Avtosalon("Zargarlik","Uchtepa tumani 11-mavze",998915750001)
Avtosalon1.add_car(avto1)
Avtosalon1.add_car(avto2)
Avtosalon1.add_car(avto3)
a = Avtosalon1.amount_cars
print(a)
j=1
b=Avtosalon1.show_cars()
for i in Avtosalon1.show_cars():
    print(f"{j}) ",i)
    j+=1

Avtosalon1.delete_car(avto3)
a = Avtosalon1.amount_cars
b=Avtosalon1.show_cars()
print(a)
j=1
for i in Avtosalon1.show_cars():
    print(f"{j}) ",i)
    j+=1

