#kitoblar =[]
#savol = "Yoqtirgan kitoblaringizni kiriting: "
#savol+= "('stop' so'zini kiritsangiz amaliyot to'xtatiladi.)\n"
#hile True:
#    qiymat = input(savol)
#    if qiymat == 'stop':
#       break
#    else:
#        print(qiymat)

#savol = "Yoshingizni kiriting: "
#savol0 = "'exit' yoki 'quit' tugmalari bosilsa amaliyot yakunlanadi. " 
#while True:
#    print(savol0)
#    yosh = input(savol)
#    
#    if str(yosh)=='exit' or str(yosh)=='quit':
#       break
#    else:
#        if int(yosh)<7:
#            price = 2000
#           y = "7 yoshdan kichik"
#       elif 7<=int(yosh)<=18:
#               price=3000
#                y = "7 yoshdan 18 yoshgacha"
#        elif 18<int(yosh)<=65:
#                    price = 10000
#                   y ="18 yoshdan 65 yoshgacha"
#       else:
#                       price = 0
#                       y = "65 yoshdan kattalar"
#       print(f"\n{y} mehmonlar uchun chipta narxi {price} so'm")

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if  qiymat.title()=='Exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")