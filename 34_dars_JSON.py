import json

# 34_dars_JSON_bilan_ishlash, amaliyot:
# 1-vazifa:    
# Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring:
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}


data ={
       'model':'malibu',
       'rang':'qora',
       'yil':2000,
       'narx':40000
       }
data_json=json.dumps(data)
#print(data_json)
#print(type(data_json))
#print(type(data))


# Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring:
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
# 2-vazifa:
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""    
talaba=json.loads(talaba_json)
#print(talaba['ism'],talaba['familiya'])
#print(type(talaba))
#print(type(talaba_json))

# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
# 3-vazifa:
    
with open('34d_json','w') as fayl_34:
    json.dump(data,fayl_34)
with open('34d_json','a') as fayl_34:
    json.dump(talaba,fayl_34)

    
# Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan.
# Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi"
# ko'rinishida konsolga chiqaring.
# 4-vazifa:

with open('students.json','r') as std:
    students=json.load(std)
#for i in students['student']:
#    print(f"{i['name'].title()} {i['lastname'].title()} {i['year']}-course, student of {i['faculty'].title()} faculty")


# Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash tili haqidagi
# maqolani JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan ma'lumotni
# JSON ko'rinishida saqlang (brauzerda Ctrl+S tugmasini bosib).
# Faylni Pythonda oching va konsolga maqolaning sarlavhasi (title)
# va qisqa matnini (extract) chiqaring:
# https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python
# 5-vazifa:
dd={
  "batchcomplete": "",
  "query": {
    "pages": {
      "13801": {
        "pageid": 13801,
        "ns": 0,
        "title": "Python",
        "extract": "Python ([ˈpʌɪθ (ə)n] — payton, piton) — turli sohalar uchun yuqori darajadagi umumiy maqsadli dasturlash tili. Uning dizayn falsafasi muhim chekinishdan foydalangan holda kodning oʻqilishiga urgʻu beradi. Uning til konstruksiyalari va obyektga yoʻnaltirilgan yondashuvi dasturchilarga kichik va yirik loyihalar uchun aniq, mantiqiy kod yozishda yordam berishga qaratilgan. Shuningdek Python sunʼiy intellekt hamda maʼlumotlar muhandisiligi sohalarining tili hisoblanadi.\nPython deyarli barcha platformalarda ishlay oladi, xususan Windows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar shular jumlasidandir. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud boʻlib, uning nomi — IronPython dasturlash muhitidir.\nGuido van Rossum 1980-yillarning oxirida ABC dasturlash tilining davomchisi sifatida Python ustida ishlay boshladi va birinchi marta 1991-yilda Python 0.9.0 versiyasini ommaga eʼlon qildi.\nPython dasturlash tiliga boʻlgan talab yildan yilga oshib bormoqda. CodingDojo portalining tadqiqotlariga koʻra, 2020—2021-yillarda aynan Python tilida dasturlovchi mutaxassislarga eng koʻp talab boʻlgan."
      }
    }
  }
}
with open('api_result1.json','w') as f:
    json.dump(dd,f)
  
with open('api_result1.json','r') as ff:
    dd=json.load(ff)
    
print(dd['query']['pages']['13801']['title'])
print("________________________")
print(dd['query']['pages']['13801']['extract'])










