print("Ali\'nin yanındaydım") # \ kendinden sonraki karakteri özel olarak nitelendirmez

print("""Merhaba
dünya""") #"""""" satırda nasıl yazarsa öyle alır

print("Merhaba\nDünya") # \n alt satıra geçiş yapar

print("Merhaba \tDünya") # \t tab tuşu gibi davranır

mesaj = "merhaba dünya" # giriş ekleme
print(mesaj) # mesaj girişini çalıştırır

mesaj1 = "merhaba"
mesaj2 = "dünya"
print(mesaj1 + " " + mesaj2) # mesaj1 ve mesaj2 birleşir

mesajj = "Mesajlama"
print(mesajj[2]) # mesajj girişindeki 2. harfi yazdırır
print(mesajj[0:3]) # 0 ve 3. karakter arası harfleri yazdırır
print(mesajj[::2]) # 2şer 2şer harfleri yazdırır
print(mesajj.upper()) # harfleri büyütür
print(mesajj.lower()) # harfleri küçültür
print(mesajj.capitalize()) # baş harfi büyütür
print(mesajj.startswith("Me")) #kelime başlangıcını true false olarak yanıtlar
print(len(mesajj)) # kaç kelimeden oluştuğunu verir

print("merhaba" * 10) # 10 kez merhaba yazar

isim = "ali"
yas = "20"
print("{} , {} yaşındadır.".format(isim , yas)) # format ile sıralı kümelere giriş verilir
print(f"{isim} , {yas} yaşındadır.") # f ile küme içine girişler yazılabilir
