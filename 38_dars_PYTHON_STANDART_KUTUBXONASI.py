import datetime as dt
import math
import pprint
import re

# 38_dars_PYTHON_STANDART_KUTUBXONASI
# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
# 1-vazifa:
bugun=dt.date.today()
day=14
#for i in range(0,10):
#    farq=dt.date(2025,10,day)
#    print(farq.strftime("%d--%B--%Y"))
#    day+=1
    

# Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
# 2-vazifa:
keyingi_ramazon_hayiti=dt.date(2026,3,20)
keyingi_qurbon_hayiti=dt.date(2026,5,26)
#print(f"Kelgusi Ramazon hayiti kunigacha {(keyingi_ramazon_hayiti-bugun).days} kun qoldi.")
#print(f"Kelgusi Qurbon hayiti kunigacha {(keyingi_qurbon_hayiti-bugun).days} kun qoldi.")

# Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun
# o'tganini qaytaruvchi funksiya yozing
# 3-vazifa:
def calculate_days(year,month,day):
    if bugun.month>=month:
        difference_year=bugun.year-year
    else:
        difference_year=bugun.year-year-1
        
        
    
    if bugun.month>month:
        difference_month=bugun.month-month
    elif bugun.month<month:
        difference_month=bugun.month+12-month
    else:
        difference_month=0
    if bugun.day>day:
        difference_day=bugun.day-day
    elif bugun.day<day:
        if int(bugun.month) in [1,3,5,7,8,10,12]:
            difference_day=bugun.day+31-day
        elif bugun.month==2 and bugun.year%4==0:
            difference_day=bugun.day+29-day
        elif bugun.month==2 and bugun.year%4!=0:
            difference_day=bugun.day+28-day
        else:
            difference_day=bugun.day+30-day
    else:
        difference_day=0
  
    difference=[difference_year,difference_month,difference_day]
    print(f"{year}-yil {month}-oy {day}-sanada tug'ulgan inson"
          f" hozirda {difference[0]} yosh {difference[1]} oy"
          f" {difference[2]} kunlik hisoblanadi.")

#calculate_days(1999,12,24)

# Foydalanuvchidan telefon raqamini kiritishni so'rang.
# Kiritlgan qiymatni andoza yordamida tekshiring
# 4-vazifa:
andoza="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
#while True:
#    phone_num=input("Telefon raqamingizni kiriting: ")
#    if re.match(andoza, phone_num):
#        print("RAXMAT!")
#        break
#    else:
#        print("Kiritilgan ma'lumot mos emas. Iltimos to'g'ri kiriting.")








