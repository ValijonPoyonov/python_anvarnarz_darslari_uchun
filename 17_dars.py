orders = []
ishora = True
while ishora:
    order = input("Buyurtmani kiriting: ")
    orders.append(order)
    answer  = input('Yana buyurtma berishni istaysizmi? (ha/yo\'q)')
    if answer=='ha':
        continue
    else: ishora=False
print(orders)

#products={}
#savol = "E-bozor uchun maxsulotlar ro'yxatini kiriting.\n"
#savol+= "(amaliyotni yakunlash uchun 'stop' buyrug'ini kiriting)" 
#m=1
#while True:
#   product = input(f"{savol}\n{m}-maxsulot: ")
#   if product=='stop':
#       break
#   price = int(input('maxsulotning narxi: '))
#   products[product]=price
#   m+=1
#for k,v in products.items():
#    print(f"{k.title()} ning narxi {v} so'm")
    
products_e_bozor={
    'non':3000,
    'suv':2000,
    'yog\'':22000,
    'go\'sht':105000,
    'kartoshka':5200,
    'sabzi':2700,
    'ko\'kat':1500
    }
while orders:
    check = orders.pop()
    if check in products_e_bozor:
        print(f"{check.title()} bor, {products_e_bozor[check]} so'm")
    else:
        print(f"{check.title()} hozircha e-bozorda yo'q")
        