# print("          ATTO     ")
# print("       NAQT TOLOV      ")
# print("      QOQON ANDIJON     ")
# import datetime

# x = datetime.datetime.now()

# print("sana   ", x.strftime("%X"))

# import random 

# random_number = random.randint(10,99)
# print("ch:  ", random_number + 10000000000000)


# print("NARXI:  15000 som" )

# usd_uzs = 12907.51
# usd = float(input("kursni kirit >>>"))
# uzs = usd * usd_uzs
# print(f"{usd} USD = {uzs} UZS (kurs: {usd_uzs} UZS)")

# t_yil = int(input("tugilgan yilingizni kiriting\n>>>"))
# yosh = 2025 - t_yil
# print("Siz ", yosh, "Yoshda ekansiz" )

# son = int(input("Sonni kirit\n>>>"))
# son1 = son**2
# son2 = son**3
# print(son, "Kvadrati", son1, "Teng  \n", son, "kubi", son2, "Teng" )

# yilingiz = int(input("Yoshingizni kiriting\n>>>"))
# yosh = 2024 - yilingiz
# print("siz", yosh, "yilda tugigansiz")

# son1 = int(input("Birinchi Sonini Kiriting\n>>>"))
# son2  = int(input("Ikkinchi sonni kiriting\n>>>>"))
# jami = son1 + son2
# jami2 = son1 - son2
# jami3 = son1 * son2
# jami4 = son1 // son2

# print("Qoshilgada", jami)
# print("Ayrilganda", jami2)
# print("Kopaytrilganda", jami3)
# print("Bolinganda", jami4)

# ismlar = ["sardor", "Akbar", "Jama"]
# print(ismlar[0], "Bugun choyxonaga boramizmi")
# print(ismlar[1], "Bugun choyxonaga boramizmi")
# print(ismlar[2], "Bugun choyxonaga boramizmi")

# sonlar = [10000,18000,8999,2333,12.12]
# print(sonlar[1] // 1000)


# t_shaxs = ["Alisher Navoiy", "Zahitiddind Muahammad Bobur", "amir Temur"]
# z_shaxs = ["Akbar", "Zehni", "Salohhid"]

# print("Men tarixiy shaxslardan", t_shaxs.pop(2), "\nYaxshi korib tarixlarini oqiyman va zamonaviy shaxslardan "
#       , z_shaxs.pop(1), "shu  odamlarni taniyman va ancha malumotga egaman")
# friends = []
# friends.append('John')
# friends.append('Alex')
# friends.append('Danny')
# friends.append('Sobirjon')
# friends.append('Vanya')
# friends.remove('John')
# friends.insert(0, "reks")
# friends.insert(5, "kozim")

# mehmonlar = []
# mehmonlar.append(friends.pop(2))

# print(mehmonlar)


# juft_son = list(range(120, 1200, 2))
# print(max(juft_son) - min(juft_son) )
# print(sum(juft_son))
# print(juft_son[0:20])
#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# nonushta.remove('norin')
# nonushta.remove('shashlik')
# nonushta.remove('qozonkabob')
# nonushta.append('non va qaymoq')
# nonushta.append('issiq non')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar)
# print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"


# ismlar = ['Akbar', 'Yunus', 'Ali', 'Vali', 'Bexruz']
# for ism in ismlar:
#     print(f"{ism} Salom")
#     print('Ismlar',len(ismlar), 'marta takrorlandi')


# toq_sonlar = list(range(1,100,2))
# for t_son in toq_sonlar:
#     print(f"{t_son**3} ")


# kinolar = []
# print("5ta eng sevimli kinolarizni yozin")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1} - sevgan kinoingiz:  "))
# print(kinolar)
    
# dostlar = []
# print("Bugun kimlar bn suhbatlashtingiz")
# for dost in range(5):
#     dostlar.append(input(f"{dost+1} - suhbatlashgan insoningiz:  "))
# print(dostlar)


# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
    
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
 
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
 
# for car in cars:
#     if car != 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# ism = input('Loginingizni Kiriting?\n>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() == 'admin': # Agar ism Aliga teng bo'lmasa ...
#     print("Xush kelibsiz admin") # quyidagi xabar chiqadi
# else:
#     print("xush kelibsiz foydalanuvchi")

# son1 = int(input("1 chi sonnini kiriting>>>"))
# son2 = int(input("2 chi sonni kiriting>>>"))

# if son1 == son2:
#     print("bu sonlar teng")
# if son1 > son2:
#     print("1 chi kiritgan soniz kotta")
# if son1 < son2:
#     print("2 ch ikiritgan soniz kotta")


# son1 = int(input("1 chi sonnini kiriting>>>"))

# if son1<0:
#     print("bu son musbat")
# if son1>0:
#     print("bu son manfiy")


# son = float(input('Istalgan son kiriting: '))
# print(son**(1/2)) if son>0 else print('Musbat son kiriting')
# Yaxshi ko'rgan va o'qilgan kitoblarni saqlash uchun ro'yxatlar



# yaxshi_korgan_kitoblar = []
# oqilgan_kitoblar = []

# # 5 ta kitobni kiritish
# print("Yaxshi ko'rgan 5 ta kitobingizni kiriting:")
# yaxshi_korgan_kitoblar = [input(f"{i + 1}-kitob nomi: ") for i in range(5)]

# # Barcha yaxshi ko'rgan kitoblar bosh ro'yxatga kiritiladi
# bosh_kitoblar = yaxshi_korgan_kitoblar.copy()

# # O'qilgan kitoblarni kiritish
# print("\nSizning yaxshi ko'rgan kitoblaringiz:")
# for i, kitob in enumerate(yaxshi_korgan_kitoblar, 1):
#     print(f"{i}. {kitob}")

# print("\nYuqoridagi kitoblar ichida o'qiganlaringizni tanlang:")
# oqigan_kitoblar_nomi = [
#     input(f"{i + 1}-kitobni o'qigan bo'lsangiz nomini yozing (agar o'qimagan bo'lsangiz ENTER bosing): ")
#     for i in range(5)]

# # O'qilgan kitoblarni ajratish va bosh ro'yxatga kiritish
# for kitob in oqigan_kitoblar_nomi:
#     if kitob and kitob in yaxshi_korgan_kitoblar and kitob not in oqilgan_kitoblar:
#         oqilgan_kitoblar.append(kitob)
#         if kitob not in bosh_kitoblar:
#             bosh_kitoblar.append(kitob)

# # Natijalarni ko'rsatish
# print("\nSizning yaxshi ko'rgan kitoblaringiz:")
# print(", ".join(yaxshi_korgan_kitoblar))

# print("\nSiz o'qigan kitoblaringiz:")
# print(", ".join(oqilgan_kitoblar))

# print("\nBosh kitoblar ro'yxati (hammasi):")
# print(", ".join(bosh_kitoblar))



# yosh = int(input("Yoshingiz nechida>>>"))

# if yosh <= 4:
#     print("siz uchun hayvonot bogikrish bepul")
# elif yosh <=12:
#     print("Siz uchun kirish 5000som")  
# else:
#     print("siz uchun kirish 10000som")


# kun = input("Bugun qaysi kun")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dm olish kuni")
# else:
#     print("Bugun dars boladi")

# kun = input("Bugun nma kun>>>")
# harotat = float(input("Havo harorati qanday>>>"))

# if kun.lower() == 'yakshanba' and harotat >= 30:
#     print("Chomilosang boladi")
# elif kun .lower() == 'shanba' and harotat < 30:
#     print("Uyda dam olasan")


# menu = ['manti', 'osh','shorva', 'norin']

# ovqat = input("NIma ovqat yiysiz>>>")
# if ovqat.lower() in menu:
#     print("ovqat qabul qilindi")
# else:
# #     print("Kechirasiz bu ovqat bizning menuda yoq")



# son = float(input("Juft son kiriting: "))
# if son%2!=0:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")

# yosh = int(input("Yoshingizni yozing:  "))
# if yosh <= 4 or yosh >= 60:
#     print("Siz uchun kirish tekin")
# elif yosh < 18:
#     print('Siz uchuh kirish 10000som')
# elif yosh > 18:
#     print('siz uchun kirish 20000som')



# son1 = float(input("1 chi sonni kiriting>>>"))
# son2 = float(input("2 chi sonni kiriting>>>"))


# if son1 == son2:
#     print('bu sonlar teng')
# elif son1 > son2:
#     print(f"{son1} kotta")
# elif son1 < son2:
#     print(f"{son2} kota")
    
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

# foydalanuvchilar = ['anvar', 'behruz', 'shokir', 'komil', 'nodir']
# foydalanuvchi = []
# for n in range(1):
#     foydalanuvchi.append(input("Yangi login tanlang>>> "))
# if foydalanuvchi:
#     for foydalanuvchilar in foydalanuvchi:
#         if foydalanuvchilar in foydalanuvchi:
#             print(f"Bu {foydalanuvchilar} login band")

# users = ['alisher1983','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")

# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


# talaba = {'ism':'behruz', 'familiya':'isroilov', 'tugilgan yili':2006 }

# print(f"Talaba {talaba['ism'].title()} {talaba['familiya']} u {talaba['tugilgan yili']} da tugilgan")


# otam = {'ismi':'ravshanbek', 't_yil':1979, 'shahri':'fargona', 'kochasi':'mashal'}
# onam = {'ismi':'hurixon', 't_yil':1981, 'shahri':'fargona', 'kochasi':'mashal'}



# print(f"otamni ismi {otam['ismi'].title()} {otam['t_yil']} -yilda tugilgan {otam['shahri'].title()} shahrida tugilgan {otam['kochasi'].title()} kochasida turadi")
# print(f"onami ismi {onam['ismi'].title()} {onam['t_yil']} - yilda tugilgan {onam['shahri'].title()} shahrida tugilgan {onam['kochasi'].title()} kochasida turadi")

# oila = {
#         'ism1':'ali',
#         'y_taom1':'osh',
#         'ism2':'vali',
#         'y_taom2':'shorva',
#         'ism3':'gani',
#         'y_taom3':'manti',
#         'ism4':'anvar',
#         'y_taom4':'mastava',
#         'ism5':'abdu',
#         'y_taom5':'mastava'
#         }
# print(f"{oila['ism1'].title()} ning yaxshi korgan ovqati {oila['y_taom1']}")
# print(f"{oila['ism2'].title()} ning yaxshi korgan ovqati {oila['y_taom2']}")
# print(f"{oila['ism3'].title()} ning yaxshi korgan ovqati {oila['y_taom3']}")
# print(f"{oila['ism4'].title()} ning yaxshi korgan ovqati {oila['y_taom4']}")
# print(f"{oila['ism5'].title()} ning yaxshi korgan ovqati {oila['y_taom5']}")

# lugat = {
#     'apple':'olma',
#     'pineapple':'nok',
#     'banana':'banan',
#     }
# kirit = input("Kalit sozni kirit:  ")
# chiq = lugat.get(kirit,'Bunday ism mavjud emas')

# print(chiq)

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    

# izoh_lugat = {
#     'boolean':'mantiqiy qiymat',
#     'float':'onlik son',
#     'for':'biror amalni qayta qayta takrorlash tsikli',
#     'if':'shartlarn tekshirish operatori',
#     'interger':'butun son'
#     }


# for izoh in sorted(izoh_lugat):
#     print(izoh)
    
# for izohh in sorted(izoh_lugat.values()):
    
#     print(izohh)



# from tkinter import *


# # Tk() bu yerda konstrukter deyladi
# window = Tk() 

# # title() bu yerda sarlavha oynasi deyiladi
# window.title("sarlavha oynasi dasturini")

# # geometry(500x500) esa bunda oyanani olchamlarini belgilaydi
# window.geometry("500x500")

# cliks = 0

# def click():
#     global cliks
#     cliks += 1
#     buttonText.set("Cliks {}".format(cliks))
# buttonText = StringVar()

# # button() bu yerda oynaga knopka qosish uchun ishlatiladi
# btn = Button(textvariable=buttonText, text="salom", background="red", foreground='yellow', padx='50', pady='10', font=('arial', 20), activebackground='green', bd=10, command=click)
# # pack() bu yerda knopkani korsatish uchun ishjlatiladi
# btn.pack(expand=True,  side=BOTTOM)

# # button() bu yerda oynaga knopka qosish uchun ishlatiladi
# btn2 = Button(textvariable=buttonText, text="salom", background="red", foreground='yellow', padx='50', pady='10', font=('arial', 20), activebackground='green', bd=10, command=click)
# # pack() bu yerda knopkani korsatish uchun ishjlatiladi
# btn2.pack(expand=True,  side=TOP)


# # button() bu yerda oynaga knopka qosish uchun ishlatiladi
# btn3 = Button(textvariable=buttonText, text="salom", background="red", foreground='yellow', padx='50', pady='10', font=('arial', 20), activebackground='green', bd=10, command=click)
# # pack() bu yerda knopkani korsatish uchun ishjlatiladi
# btn3.pack(expand=True, side=LEFT)


# # button() bu yerda oynaga knopka qosish uchun ishlatiladi
# btn4 = Button(textvariable=buttonText, text="salom", background="red", foreground='yellow', padx='50', pady='10', font=('arial', 20), activebackground='green', bd=10, command=click)
# # pack() bu yerda knopkani korsatish uchun ishjlatiladi
# btn4.pack(expand=True,  side=RIGHT)





# # mainloop() bu yerda oynanni chiqarish uchun ishlatiladi
# window.mainloop() 


# adabiyot = {
#     'abu abdulloh muhammad ibn ismoil ':['Al-jome','as-sahih', 'al-adab'],
#     }

# for ism, tillar in adabiyot.items():
#     print(f"\n{ism.title()} mashxur asarlari: ")
#     for til in tillar:
#         print(til.upper())




# son = 1
# while son<=5:
#      print(son, end=' ')
#      son += 1
# print('son tugadi')





# print('Kiritilgan soni kvatradini hioblovchi dastur')
# savol = 'Istalgan soni kiriting '
# savol += "(dasturni toxtatish uchun 'exit' deb yozing) : "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
        

# 2chi 




# print('Kiritilgan soni kvatradini hioblovchi dastur')
# savol = 'Istalgan soni kiriting '
# savol += "(dasturni toxtatish uchun 'exit' deb yozing) : "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("dastur toxtadi")
        

# amaliyot while

# kirit = 'yaxshi korgan kitobingizni kiriting'
# kirit += 'dasturni toxtatish uchun "stop" sozin yozing: '
# qiymat  = ''
# while qiymat != 'stop':
#     qiymat = input(kirit)
# print('dastur toxtadi')


# # 2

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")
# print("datur toxtadi")


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    