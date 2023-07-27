class futbolcu: # class oluşturduk
    def __init__(self, isim, soyisim, yas): # fonksiyon açtık
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    def __eq__(self, other): # fonksiyon açtık. bu fonksiyonda isim ve soyisim eşit olup olmadığı sorgulanıyor,
        if self.isim == other.isim and self.soyisim == other.soyisim: # eğer eşitse,
            return True # True çıktısı verecek
        return False # değilse False çıktısı verecek
    def __add__(self, other): #fonksiyon oluşturduk. bu fonksiyonda isim ve soyisim ilk harflerini toplayacağız
        isim = self.isim[0] + other.isim[0] # isim1 ve isim2 ilk ahrfleri alındı ve isim adı altında alındı
        soyisim = self.soyisim[0] + other.soyisim[0] # soyisim1 ve soyisim2 ilk ahrfleri alındı ve soyisim adı altında alındı
        yas = self.yas  + other.yas # yaşlar toplanıp yas adı altında alındı
        return futbolcu(isim, soyisim, yas) # yeni bir futbolcu oluşturuldu
    def __lt__(self, other): # fonksiyon açtık. bu fonksiyonda 1. ve 2. kişinin yaşları karşılaştırıldı.
        if self.yas < other.yas: # 1. < 2. 
            return True # True çıktısı
        return False #false çıktısı
    

futbolcu1 = futbolcu("ahmet", "veli", 25) # futbolcu1 eklendi
futbolcu2 = futbolcu("hakan", "fidan", 20) # futbolcu2 eklendi

futbolcu3 = futbolcu1 + futbolcu2 #futbolcu1 + futbolcu2 toplama fonksiyonu ile toplanıp futbolcu 3 oluşturuldu.
print(futbolcu3.yas) # futbolcu3 yaşı yazdırıldı

print(futbolcu2 < futbolcu1) # futbolcu1 ve futbolcu2 karşılaştırma fonksiyonu ile karşılaştırılıp çıktı alındı