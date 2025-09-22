

# 33_dars_FAYLLAR_BILAN_ISHLASH
# Amaliy vazifalar
# 1-vazifa: Bugun o'rgangan narsalaringizni matnga yozing va matnni Python
# yordamida oching

with open('33_dars_yozma.txt') as file:
    matn = file.read()



# 2-vazifa: Quyidagi pi_million_digits.txt faylini yuklab oling
# (faylda π soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 
fayl = open('pi_million_digits.txt')
text = fayl.read()
#print(text)
fayl.close()
# 3-vazifa: Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q ekanligini
# aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral,
# 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
#with open('pi_million_digits.txt') as strpi:
#    r = strpi.read()
#    info = "Tug'ulgan kuningizni quyidagicha ko'rinishda kiriting:"
#    info += "17-mart 1999-yil >>> '17031999' :"
#    birth_digits = input(info)
#    if birth_digits in r:
#        print("Sizning tug'ulgan kuningizni sanasi pi sonini millionta honasini ichida bor ekan.")
#    else:
#        print("Sizning tug'ulgan kuningizni sanasi pi sonini millionta honasini ichida yo'q ekan.")

# 4-vazifa:
# Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle
# yordamida yangi faylga saqlang.
import pickle
with open('sinov.txt') as sinov:
    s = sinov.read()
#print(s,type(s))
s=s.replace(" ","")
s=s.replace('\n',"")
s=float(s)
#print(s,type(s))
with open('picklefayl','wb') as fayl:
    pickle.dump(s, fayl)
with open('picklefayl','rb') as fayl2:
    fayl2 = pickle.load(fayl2)
#print(fayl2)


# 5-vazifa:
# Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni
# yangi qatordan faylga yozib boruvchi dastur tuzing.
# Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan
# qo'shilib borsin (yangi faylga emas).

def registor():
    print("Assalom alaykum. Iltimos sizni ro'yxatga olishimiz uchun quyidagi"
          " ma'lumotlarni kiriting.")
    name=input("Ismingiz: ")
    surname=input("Familiyangiz: ")
    phone=input("tel: ")
    address=input("Manzil(vil,tum,ko'cha,uy raqami): ")
    info = name.title()+" "+surname.title()+", "+phone+", "+address.title()+"."
    return info
def save_info():
    n=0
    with open('user_info','a') as file:
        info=registor()
        file.write(info)
        file.write('\n')
        n+=1
    print(f"Hozirda faylda {n} ta foydalanuvchi haqida ma'lumot bor.")
def watch_file(fayl):
    with open(fayl,'r') as f:
        f=f.read()
    return f
#save_info()
#print(watch_file('user_info'))



