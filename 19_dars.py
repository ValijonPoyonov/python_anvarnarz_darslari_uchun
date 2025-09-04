def yosh_hisobla():
    ism = input("Ismingizni kiriting: ")
    tyil = input('Tug\'ilgan yilingizni kiriting: ')
    print(f"{ism.title()}, siz {2025-int(tyil)} yoshdasiz!")
#yosh_hisobla()

def salom_ber():
    print("Assalomu alaykum!")
        

def daraja_hisobla():
    """Foydalanuvchidan biror sonni olib,
    uning darajasini va kubini hisoblovchi f-ya"""
    son = input("Biror son kiriting: ")
    kv = float(son)**2
    kub = float(son)**3
    print(f"Siz kiritgan sonning kvadrati {kv} ga, kubi esa {kub}  ga teng.")
    
#daraja_hisobla()

def juft_toqni_aniqla():
    son = int(input("Assalom alaykum, birorta musbat butun sonni kiriting: "))
    if son%2==0:
        print("Siz kiritgan son juft son.")
    else:
        print("Siz kiritgan son toq son.")
#juft_toqni_aniqla()
def kattasini_chiqar():
    print("Istalgan ikkita son kiriting: ")
    x=float(input("1-son:"))
    y=float(input("2-son:"))
    if x>y:print(x)
    elif x<y: print(y)
    else: print("Kiritilgan sonlar o'zaro teng.")
#kattasini_chiqar()
def darajaga_kotar(x,y=2):
    """Foyadalanuvchidan x va y sonlarini olib,
    x ning y inchi darajasini hisoblovchi f-ya"""
    d = x**y
    return d
#a = darajaga_kotar(4)
#print(a) 

def bolinishni_tekshir(son):
    n=0
    for i in range(2,10):
        if son%i==0:
            print(f"{son} {i}ga qoldiqsiz bo'linadi.")
            n=n+1
    if n==0:print(f"{son} tub son.")
bolinishni_tekshir(43)