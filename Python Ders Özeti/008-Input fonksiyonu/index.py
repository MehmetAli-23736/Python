sayi = input("bir sayı giriniz") # input -> terminalden veri almaya yarar. string çıktısı verir. İnteger'a ceçrilmesi gerekir.
print(sayi)

faktoriyel = 1

for i in range(1, sayi+1): # faktöriyel almak için bir döngü açıyoruz.
    faktoriyel *= i
    print(f"{sayi}! = {faktoriyel}") # x! = x faktöriyel olarak çıktı verir
    

i = 2 
while i<= sayi: # while döngüsü ile faktöriyel alma örneği
    faktoriyel *= i
    i += 1
    print(f"{sayi}! = {faktoriyel}") # çıktı olarak alırız
    

prime = True  # asal olup olmama örnek kodu
for i in range(2, sayi): # sayi giriş olarak ayarlanmıştı.
    if sayi %i == 0:
        prime = False
        break
if prime == True:
    print(f"{sayi} sayısı asaldır") # asal ise burası çalışır
else:
    print(f"{sayi} sayısı asal değildir") # asal değil ise burası çalışır
    


    


    
    
