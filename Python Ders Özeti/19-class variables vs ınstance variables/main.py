class calisan:
    personel_sayisi = 0 # personel sayısı isimlendirilir
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas
        calisan.personel_sayisi += 1 # her veri eklendiğinde 1 artar
        

print(calisan.personel_sayisi) # sayı 0
calisan1 = calisan("mehmet", 1000) #1. eklendi
print(calisan.personel_sayisi) # sayı 1
calisan2 = calisan("ahmet", 3000) # 2. eklendi
print(calisan.personel_sayisi) #sayı 2