#key-value ilişkisi

kisi = {"isim" : "ali", "yas" : "20", "cinsiyet" : "m", "hobiler" : ["sinema", "konser", "yazılım"]} # küme ile key-value ilişkisine uygun
print(kisi) # hepsini yazdırır
print(kisi["isim"]) #sadece isim verisi yazdırılır.

kisi["isim"] = "ahmet" # kisi kümesindeki isim ali yerine ahmet oalrak değiştirildi
kisi.update({"isim" : "ahmet", "yas" : 30}) # kümede birden fazla veri güncelleme için kullanılır
kisi["id"] = 12345 # yeni bir key(anahtar)eklendi
del kisi["id"] # kümedeki id keyi silinir

for x in kisi: # for döngüsü ile yazdırma.
    print(x) # sadece keyler verilir
    
    print(kisi[x]) # sadece value yazdırılır
    print(kisi.keys()) #sadece keyler küme içine yazılır
    print(kisi.values()) #sadece valueler küme olarak yazdırıldı
    print(kisi.items()) # içerik, farklı kümeler ile yazdırıldı
    print(kisi["soyad"]) # kümede soyad keyi olamdığı için hata alınır
    print(kisi.get("soyad")) # kümede soyad keyi yok ama hata da vermedi
