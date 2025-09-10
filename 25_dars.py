# Anvar Narzullayev, 25-dars "Son topish o'yini", foydalanuvchi va kompyuter orasida 
# o'yin tashkillashtirish.
import random
print("Assalom alaykum hurmatli foydalanuvchi, keling siz bilan 'Son topish' o\'yinini o\'ynaymiz. "
      "Men 1 dan 10 gacha bo\'lgan oraliqda biror sonni o\'ylayman, siz uni topishga  harakat "
      "qilasiz, keyin men siz o\'ylagan sonni topishga harakat qilaman, kim kamroq urinishda topsa "
      "o\'sha o'yinni yutgan hisoblanadi. 1 ni ham 10 ni ham o'ylash mumkin!")
javob = int(input("Agar o'ynamoqchi bo'lsangiz ishora qiling.(ha(1)/yo'q(0)):  "))
if javob==1:
    son_k = random.randint(1, 10)
    n=1
    son_f = int(input("Unda boshladik men bir son o'yladim, topishga harakat qiling: "))
    while True:
        if son_f==son_k:
            print(f"\n<<<<<To'gri, men o'ylagan son {son_f} edi, siz {n} ta urinishda topdingiz.>>>>>")
            user_urinishlari = n
            break
        elif son_f>son_k:
            son_f = int(input("Men o'ylagan son kichikroq. Yana bir bor urinib ko'ring: "))
            n=n+1
        else:
            son_f = int(input("Men o'ylagan son kattaroq. Yana bir bor urinib ko'ring: "))
            n=n+1
    print("Endi siz oraliqdagi birorta sonni o'ylang men topishga harakat qilaman.")
    ishora = int(input("Ha o'yladim(1), yo'q o'yanashni hohlamayman(0): "))
    if ishora == 1:
        n=1
        list_1 = list(range(1,11))
        k=random.choice(list_1)
        print(f"\n<<<---{k}--->>> shu sonni o'yladingizmi? Topdimmi?\n")
        while True:
            print("To'g'ri, men shu sonni o'ylagan edim(0)\n"
                  "Noto'g'ri, kattaroq son edi(+).\n"
                  "Noto'g'ri, kichikroq son edi(-).\n")
            reply = input("")
            i=0
            if reply=="0":
                komp_urinishlari = n
                print(f"\nBarakalla! {n} ta urinishda topding.")
                print(f"DASTUR: men {komp_urinishlari} ta urinishda topdim.\n"
                      f"Siz {user_urinishlari} ta urinishda topdingiz.\n")
                if user_urinishlari>komp_urinishlari:
                    print("Yuqoridagi natijalarga ko'ra men g'olib bo'ldim.")
                elif user_urinishlari<komp_urinishlari:
                    print("Yuqoridagi natijalarga ko'ra siz g'olib bo'ldingiz.")
                else:
                    print("Yuqoridagi natijalarga ko'ra durrang bo'ldi.")
                
                break
            elif reply=="+":
                n+=1                
                while int(list_1[i])<=int(k):
                    del list_1[i]
                k=random.choice(list_1)
                print("\nNoto'g'ri, kattaroq sonni o'ylagan edim, yana bir bor urinib ko'r.\n"
                      f"<<<---{k}--->>> shu sonmi?\n")
                
            else:
                i+=1
                n+=1
                while int(list_1[-i])>=int(k):
                    del list_1[-i]
                k=random.choice(list_1)
                print("\nNoto'g'ri, men kichikroq sonni o'ylagan edim, boshqa son ayt.\n"
                      f"<<<---{k}--->>> shu sonmi?\n")
    else:
          print("Sog' bo'ling!")
else:
    print("Hayr!")
        
        