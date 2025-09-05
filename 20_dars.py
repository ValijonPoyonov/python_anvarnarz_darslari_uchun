# Anvar Narzullayev(python.sariq.dev) 20-dars "Qiymat qaytaruvchi funksiya" amaliy vazifalar
# 1-vazifa:Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
#def get_users_informetions(name,s_name,b_year,b_place,phone_n="",e_mail=""):
#    year = 2025-int(b_year)
#    user = {
#       'name' : name,
#       's_name' : s_name,
#       'b_year' : b_year,
#        'b_place' : b_place,
#        'phone_n' : phone_n,
#       'e_mail' : e_mail,
#       'year' : year
#        }
#   return user
#user = get_users_informetions('valijon','poyonov','1999','Surkhandarya','+998910000017')
#print(user)

# 2-vazifa: Yuqoridagi funksiyani while yordamida bir necha bor chaqiring,
# va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi 
# ma'lumotni konsolga chiqaring.
#customers=[]
#while True:
#    name = input("name: ")
#   s_name = input("surname: ")
#   b_year = input("birth year: ")
#   b_place = input("birth palce: ")
#   phone_n = input("phone number: ")
#   e_mail = input("email: ")
#    user = get_users_informetions(name,s_name,b_year,b_place,phone_n,e_mail)
#    customers.append(user)
#    ishora = input("Yana foydalanuvchini kiritishni hoxlaysizmi? (yes/no): ")
#    if ishora == 'no':
#        break
#print("Ro'yxatimizga quyidagi foydalanuvchilar kiritildi:")
#idd=1
#or customer in customers:
#    if customer['phone_n']:tel=customer['phone_n'] 
#    else:tel="kiritilmagan"
#    if customer['e_mail']:email=customer['e_mail'] 
#    else:email="kiritilmagan"
#    print(f"[{idd}]---{customer['name'].title()}{customer['s_name'].title()}"
#          f" {customer['b_year']}-yil {customer['b_place'].title()}da tug'ilgan, "
#          f"telefon raqami {tel}, e_mail manzili {email}.\n")
#    idd+=1
#print(customers)

# 3-vazifa: Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
#def find_max(x,y,z):
#   maxx = max(x, y, z)
#   return maxx
#print("Istalgan 3 ta son kiriting, eng kattasini aniqlab beramiz.")
#x = float(input("1-sonni kiriting: "))
# = float(input("2-sonni kiriting: "))
# = float(input("3-sonni kiriting: "))
#axx = find_max(x, y, z)
#print(f"Kiritilgan sonlar ichida eng kattasi {maxx}.")

# 4-vazifa: Foydalanuvchidan aylaning radiusini qabul qilib olib,
# uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida
# qaytaruvchi funksiya yozing
#def solve_circle(r):
#    circle = {
#        'radius':r,
#        'diameter':2*int(r),
#       'perimeter':2*3.14*int(r),
#       'surface':2*3.14*int(r)**2
#        }
#   return circle
#circle = solve_circle(4)
#print(circle)

# 5-vazifa: Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing.
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
#def tub_sonlarni_top(x,y):
#    if x<=2:
#        box = [2,3]
#       for i in range(x,y):
#           n=2
#           while n<=(i**(1/2)):
#               if (i%n)==0:
#                   break
#               else:
#                   if ((i**(1/2))-n)<1:
#                       box.append(i)
#                       break
#                    else:
#                       n=n+1
#   else:
#       box = []
#       for i in range(x,y):
#           n=2
#           while n<=(i**(1/2)):
#               if (i%n)==0:
#                   break
#               else:
#                   if ((i**(1/2))-n)<1:
#                        box.append(i)
#                        break
#                    else:
#                        n=n+1
#   return box
#natija = tub_sonlarni_top(100, 150)
#print(natija)

# 6-vazifa: Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi
# ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga
# teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi.
# Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def print_fibonachi(son):
    list_fibonachi=[1,1]
    n=len(list_fibonachi)
    while n!=son:
        list_fibonachi.append(list_fibonachi[n-1] + list_fibonachi[n-2])
        n=len(list_fibonachi)
    return list_fibonachi
natija = print_fibonachi(50)
print(natija)
