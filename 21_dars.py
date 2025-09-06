# Anvar Narzullayev 21-dars: FUNKSIYA VA RO'YXAT
# 1-vazifa: Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning
# birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 
def title_(list0):
    list1=[]
    for i in list0:
        list1.append(i.title())
    return list1
list2=['alijon','valijon','jasurbek jumagulov','ilhomjon','botir','jaloliddin']
#result = title_(list2)
#print(result)
#print(list2)
# 2-yo'li pop() operatori orqali
def title_it(list0):
    list1=[]
    while list0:
        list1.append(list0.pop().title())
    return list1
list3=['alijon','valijon','jasurbek jumagulov','ilhomjon babanov','botir','jaloliddin']

#result1 = title_it(list3)
#print(result1)
#print(list3)

# 2-vazifa: Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi
# ro'yxat qaytaradigan qilib o'zgartiring.
def title_it(list0):
    list1=[]
    while list0:
        list1.append(list0.pop().title())
    return list1
list3=['alijon','valijon','jasurbek jumagulov','ilhomjon babanov','botir','jaloliddin']

#result1 = title_it(list3[:])
#print(result1)
#print(list3)

# 3-vazifa: Darsimiz davomida yozilgan bahola funksiyasini .pop() metodidan
# foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat
# lug'at qaytaradigan qilib yozing.
def bahola(ismlar):
    baholar = {}
    j=0
    for i in ismlar:
        ism = ismlar[j]
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=int(baho)
        j+=1
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
