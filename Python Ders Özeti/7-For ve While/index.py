list = [1, 2, 3, 4, 5, 6]

for rakam in list: # for döngüsü açtık
    print(rakam) # fro döngüsü içerisinde rakam yazdırdık
    

for i in range(0, 10): #range 0dan 10a kadar olanı yazdırır. (0 dahil 10 dahil değil)
    print(i)
    
    
# 2 üzeri 10 fonksiyonu şu şekilde olur:
sonuc = 1
for a in range(0, 10):
    sonuc *= 2
    
print(sonuc)    
    
    

liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]
for harf in liste1:
    for rakam in liste2: # içi içe for döngüsü kullanımı
        print(harf, rakam)
        
        
        
liste = [1,2,3,4,5,6,7,8,9]
for a in liste:
    if i == 3:
        continue #hiçbir şey yapma, bunu atla sonraki adıma geç demek/ break döngüyü sonlandırır
    print(i)
    
    
    
liste100 = range(100)
for i in liste100:
    if i % 3 != 0: # 3'e bölünmeyenleri alma
        continue
    
    
    
x = 2
while x < 10: # x, 10 olana kadar yazdır
    print(x)
    x += 1 # x, her döngüde 1 arttır
    
    
    
u = 1 
while True:
    print(u)  #sonsuza kadar gider ama if döngüsünde 1000 yazıldığı için 1000 olunca durur.
    u += 1
    if u == 1000:
        break