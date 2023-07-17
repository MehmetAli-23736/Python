class calisanlar: # bir class oluşturuyoruz
    def __init__(self, isim="girilmemiş", soyisim="girilmemiş", yas="girilmemiş"): # fonksiyon açıyoruz ve tanımlamaları yapıyoruz.
        self.name = isim #self ile isim bilgisini alıyoruz
        self.surname = soyisim #self ile soyisim bilgisini alıyoruz
        self.age = yas #self ile yaş bilgisini alıyoruz 
        
    def show_info(self): # burda da fonksiyon oluşturuyoruz ve kişinin bütün bilgilerini yazdırmasını istiyoruz
        print(f"ismim {self.name}, soyismim {self.surname}. Yaşım {self.age}") # fonksiyon çalışırsa bilgileri yazdıracak
        
        
        
calisan1 = calisanlar("ali", "java", 20) # çalışan 1 için bilgiler giriliyor
calisan2 = calisanlar("mehmet", "python", 30) # çalışan 2 için bilgiler giriliyor

print(calisan1.name) # çalışan 1'in sadece ismini yazdırırız 

calisan1.show_info() # çalışan 1'in bütün bilgilerini yazdırırız.(show.info fonksiyonu çağrılır)
calisan2.show_info() # çalışan 2'in bütün bilgilerini yazdırırız.(show.info fonksiyonu çağrılır)