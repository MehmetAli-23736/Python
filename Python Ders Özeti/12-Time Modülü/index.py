import time # zaman modülünü import edildi

zaman = time.time() # time ayarlandı. 1 ocak 1970'den sonraki saniyeyi gösterir 
print(zaman)

baslangic = time.time() # başlangıç kayıt edildi
liste = []
for i in range(1000000): # döngü açıldı
    liste.append(i)
bitis = time.time() #döngü bitiş zamanı kayıt edildi
print(bitis - baslangic) #başlangıç ve döngü bitiş zamanı çıkartıldı


zaman1 = time.ctime() # şimdiki tarihi verir. içerisine sayı girilirse saniye cinsinden algılanır ve başlangıç itibari ile ne kadar süre çıktığı verilir
print(zaman1)


zaman2 = time.localtime() # verileri ayırarak verir.
print(zaman2)


zaman3 = time.asctime() # yukarıdaki ile aynı. fakat içerisine localtime verilirse düzgün bir veri çıktısı verir
print(zaman3)


zaman4 = time.strftime("%d:%m:%Y") # geçerli zamanı alır. istediğiniz formatta gösterir.
print(zaman4)


print("başladı")
time.sleep(3) #kodu verilen değere göre durdurur. burada 3 saniye durdurur
print("bitti")