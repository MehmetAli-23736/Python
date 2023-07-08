import random # random modülü import edildi

for i in range(1): # döngü açarak birden fazla random sayı yazabiliriz.
    print(random.random()) # random değerler verir
    print(random.uniform(10, 30)) # belirli aralıktaki değerlere göre random veri verir(sınırlar dahil değil)
    print(random.randint(1, 5)) # her iki sınır da dahil olacak şekilde rastgele değer verir 
    print(random.randrange(1, 10, 2)) #1 ve 10 arasında 2şer 2şer değer verir.(sınırlar dahil değil) 
    
    
    
liste = ["siyah", "beyaz", "Yesil", "turuncu", "mavi"]

print(random.choice(liste)) #listeden rastgele eleman seçer
random.shuffle(liste) #listeyi karıştırır

print(random.sample(liste, 3)) #rastgele 3 eleman seçer


# zar atma örnek kodu
zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(100): # zar 100 kez atılıyor
    zar = random.randint(1, 6) # rastgele sayı seçer
    zarlar[zar] += 1 # sayı zarlar listesinde 1 arttırılır
    
for zar in zarlar:
    print(f"{zar} gemle olasılığı {zarlar[zar] / 100}") # sonuçlar bu şekilde yazılıp çıktı verir