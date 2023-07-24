class futbolcu: # class açıldı
    def __init__(self,isim,soyisim,yas): #init fonksiyon oluşturuldu
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        
    def __str__(self): #str fonksiyon oluşturuldu
        return f"ad: {self.isim} soyad: {self.soyisim} yas: {self.yas}"
    
    def __repr__(self): #repr fonksiyon oluşturuldu. parametreler hakkında bilgi verir
        return "repr çalışıyor"
    
futbolcu1 = futbolcu("ali","veli",20) # futbolcu1 oluşturuldu
print(futbolcu1) # str fonksiyonu çalışır
print(repr(futbolcu1)) #repr fonksiyonu çalışır 