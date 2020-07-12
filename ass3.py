number = input("bir tam sayı giriniz: ")
toplam=0
for i in range(0,len(number)):
    toplam+= int(number[i])**len(number)

if int(number)==toplam:
    print("sayı bir Armstrong sayısı")
else:
    print("üzgünüz") 
