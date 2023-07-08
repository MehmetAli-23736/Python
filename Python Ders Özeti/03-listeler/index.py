renkler = ["siyah", "pembe", "sarı", "kırmızı", "mavi"] # listemizi oluşturduk

print(type(renkler)) # renkler tipi list olarak çıktı
print(renkler) # renkler listesini yazar
print(len(renkler)) # renkler listesinde kaç adet eleman var -> 5
print(renkler[1]) # listedeki 1. elemanı verir 
print(renkler[2:]) # 2. elemandan sona kadar yazdır
print(renkler[1:4]) # 1den 4e kadar olan elemanları yazdır
print(renkler[::2]) # 2şer 2şer elemanları verir


renkler.append("gri") # append -> renkler listesine eleman ekler
print(renkler) # yeni listeyi yazar
renkler.insert(3, "gri") # 3. elemanın yanına yeni elemanı ekle
renkler.remove("mavi") # remove -> elemanını listeden siler

renkler2 = ["turuncu", "lacivert"] # yeni liste oluşturma
renkler.extend(renkler2) # 2. listeyi, 1. listeye ekler

renkler.pop() # pop -> son elemanı siler
renkler.reverse() # listeyi tersine çevirir
renkler.sort() # düzgün sıralama yapar(azalan, alfabetik)
renkler.sort(reverse = True) # sıralamayı tersten yapar
liste2 = sorted(renkler) # listeyi sıralar ama eski listeyi bozmaz


sayilar = [1, 2 ,10, 32, 14, 9, 7]
print(min(sayilar)) # sayılar listesindeki minimum değeri verir
print(max(sayilar)) # sayılar listesindeki maximum değeri verir
print(sum(sayilar)) # sayılar listesindeki bütün elemanları toplar


print(list(enumerate(renkler))) # liste elemanlarını numaralandırır ve yazar
print(list(enumerate(renkler, start=3))) # liste elemanlarını 3ten başlayarak numaralandırır ve yazar

print("siyah" in renkler) # renkler listesinde siyah elemanı var mı -> true

stringrenkler = " ".join(renkler) # join-> birleştirme, renkler elemanlarını stringe çevir, boşluk aralarına gelecek işareti temsil eder


#stringrenkler liste olmadan eleman olarak yazılıyor, bunu liste yapmak için:
renkleryen = stringrenkler.split("-") # "-" işareti olan yerlerden elemanları böler







