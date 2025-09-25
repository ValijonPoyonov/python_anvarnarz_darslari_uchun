# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 23:16:23 2025

@author: VALIJON
"""

# Quyidagi funksiyalarni yarating, va ularning har biri uchun test dasturlarini yozing:

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
# 1-vazifa:

def find_max(x,y,z):    
    return max(x, y, z)

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini
# katta harfga o'zgatiruvchi funksiya
# 2-vazifa:
def title_it(listt):
    listt_title=[]
    for i in listt:
        listt_title.append(i.title())
    return listt_title

#print(title_it(['alibek','valibek','salomlashish odoblari kitobi','mehnat mahallasi','salomatlik sirlari']))
        
# Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya
# 3-vazifa:
def get_even_number(list_int):
    list_even_numbers=[]
    for i in list_int:
        if i%2==0:
            list_even_numbers.append(i)
    return list_even_numbers
    
list1 = [1,4,5,66,88,75,71,41,32,25,7,9,16]
#print(get_even_number(list1))
    
# Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki
# yo'q (False) qaytaruvchi funksiya yozing.

def in_Fibonachi(n):
    if n==0 or n==1 or n==2 or n==3: return True
    f=[2,3]
    ishora=True
    k=2
    while ishora:
        fk=f[k-1]+f[k-2]
        f.append(fk)
        if fk==n:
            ishora = False
            javob = True
        elif fk>n:
            ishora = False
            javob = False
        else:
            k+=1
    return javob
    
#print(in_Fibonachi(1597))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    