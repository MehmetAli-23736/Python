sayi1 = 5 #integer
sayi2 = 3.8 #float
print(type(sayi1)) # sayi1 tipi öğrenme / integer
print(type(sayi2)) # sayi2 tipi öğrenme / float


print(5 + 5) # 5+5 toplama işlemi
print(5 - 5) # 5-5 çıkarma işlemi
print(5 * 5) # 5*5 çarpma işlemi
print(5 / 5) # 5/5 bölme işlemi
print(9 // 5) # 9//5 bölmesi tam kısmı çıktısı verir
print(5 ** 5) # 5**5 üssü işlemidir
print(abs(-5)) # abs -> mutlak değer işlemi
print(round(3.7895)) # round -> yuvarlama işlemi
print(round(3.893, 3)) # nokta sonrası verecek sayı miktarı
print(3 * 5 - 6) # işlem önceliği mevcuttur


print(3 == 3) # 3, 3e eşit mi -> true (=, atama operatörü olduğu için == olarak kullanılır)
print(4 < 6) # 6, 4ten büyüktür -> true
print(1 != 2) # 1, 2ye eşit değil -> true
print(8 >= 6) # 8, 6ya eşit ya da büyüktür -> true


sayistr = "100"
sayiint = 100
print(type(sayistr)) # içeriğin tipi /string
print(type(sayiint)) # içeriğin tipi /integer
print(sayistr == sayiint) # 1. string, 2.integer olduğu için false
sayistrtoint = int(sayistr) # sayiint stringten integere çevrildi ve sayiinttoflo olarak isimlendirildi
print(type(sayistrtoint)) # sayiinttoflo tipi integer olarak çıktı verdi

sayis = "220asd" # içerisinde metin olan sayı tanımlandı
sayis2 =int(sayis) # string, integer olarak tanımlanmak isteniyor/ burada alınan hata sayis'in string olmaması. 
print(sayis2) # sayis, içerisinde metin bulundurulduğu için integer olarak çevrilmedi ve hata alınır

sayio = int(4.6) # ondalıklı sayı integere çevirilir ve sadece tam kısmı alınır
print(sayio) # sayio tam kısmı ekrana yazılır

sayia = 250 # sayia, 250 olarak ayarlandı
sayia2 = str(sayia) # sayia, stringe çevirilip sayia2 olarak atandı
print(type(sayia2)) # sayia 2, type olarak yazıldı -> string


i = 1 # 1, i olarak atandı
i = i + 2 # i += 2 olarak da yazılabilir. i sayısı +2 olarak ayarla
print(i) # i yazılır-> 3
