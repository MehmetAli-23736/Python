# def -> fonksiyon girişi, bilgi_ver-> fonksiyon ismidir
def bilgi_ver(): # fonksiyon bu şekilde açılır.
    print("fonksiyon uygulandı") # fonksiyon çağırıldığında uygulanacak işlemler
bilgi_ver() # fonksiyonu çağırıyoruz. 


def fonksiyon_bir(isim): # isim parametresi isteniyor
    print("merhaba" + isim)    
fonksiyon_bir("ali") # isim= ali olarak gönderildi.


def toplama(x, y): # 2 parametre isteniyor
    print(f"x + y = {x + y}") # çıktı
toplama(3, 6) # sıralı olarak parametrelere değer verilir


# Ortalama hesaplama örnek kodu:
def ortalama_hesapla(liste):
    toplam = sum(liste) # liste değerleri toplamı
    adet = len(liste) #liste içerisindeki veri sayısı
    ortalama = toplam / adet
    print(f"girilen değerlerin ortalaması: {ortalama}") # çıktı
ortalama_hesapla([1, 2, 3, 4, 5]) #liste şeklinde olmalı. Aksi halde hata alırız



def merhaba(mesaj, isim = "isimsiz"): # isim parametresi girilmediğinde yerine isimsiz yazdırır. Bu şekilde hata almayız
     print(f"{mesaj} {isim}.")
     
merhaba("merhaba", "ali") # hem mesaj hem de isim girilmiş. çıktı-> merhaba Ali.
merhaba("merhaba") # sadece merhaba girilmiş. çıktı-> merhaba isimsiz.



def topla(k, l):
    print(k + l) # ekrana k + l yazdırır
    return k + l # değer döndürmesi için gerekli
    
sonuc = topla(4, 11) 
print(sonuc) # none hata çıktısı almamak için fonksiyon içine return yazılmalıdır.