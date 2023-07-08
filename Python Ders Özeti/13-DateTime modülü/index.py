from datetime import date # datetime modülü import edildi

bugun = date.today() # gün verisi alındı
print(bugun)
print(type(bugun)) # tipi datetime.date olarak çıktı verir. 
print(bugun.day) # sadece gün bilgisi verir
print(bugun.month) # sadece ay bilgisi verir
print(bugun.year) # sadece yıl bilgisi verir
print(bugun.weekday()) #haftanın kaçıncı günü olduğu verisi verir



gecmisi_tarih = date(2015, 8, 13) # tarih verilir
print(gecmisi_tarih) # verilen tarih yazılır
print(gecmisi_tarih.weekday()) #o zamanlar haftanın kaçıncı günü olduğu verir


gecen_zaman = bugun - gecmisi_tarih # o günden bu güne ne kadar süre geçmiş
print(gecen_zaman)



from datetime import datetime # datetime import edildi

suan = datetime.now() # saat ile tarihi verir
print(suan)
print(suan.hour) # saat bilgisi alınabilir

print(suan.ctime()) # düzenli bir şekilde zamanı çıktı verir
print(suan.date()) # şu anki zamanı verir
print(suan.date().month) # ay bilgisi verir

gecmis_an = datetime(2014, 5, 26, 6, 45, 32, 123) # bir tarih ve zaman verir
print(suan - gecmis_an) # şu an ve geçmiş an verisi yazılır.

print(bugun.strftime("%d-%m-%Y")) # istenen değerlere göre tarihi verir


from datetime import timedelta #datetime import edildi

suanda = datetime.now # şu anın tarihi verildi
tdelta = timedelta(days=7, hours=5, seconds=69) # tdelta manuel tarih verildi