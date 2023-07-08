if True: # if işlemi doğru
    print("çalıştı") # işlem doğru olduğu için çalışacak
    
a = 5
b = 7
if a == b: # a, b'ye eşitse çalışır. matematiksel işlemler uygulanabilir
    print("a, b'ye eşittir") # a, b'ye eşit değil. bu yüzden çalışmaz.

x = 6
y = 8
if a == b:
    print("x = y")
else: # x, y'ye eşit değilse çalıştır
    print("x != y")
    
renk = "mavi"

if renk == "beyaz":
    print("beyaz")
elif renk == "sari": # bunu da dener
    print("sari")
elif renk == "yeşil":
    print("yeşil")
else:
    print("hiçbiri değil")
    
    
k = 5 
l = 6
m = 10
if k < l or m > k: # or-> veya demek(1-1)(1-0)(0-1)=true
    print("koşul doğru")
else:
    print("hatalı")

# or ->  (1-1)(1-0)(0-1)olmalı
# end -> (1-1) olmalı


liste = [1, 2, 3, 4 ,5 , 6, 7, 8, 9]
z = 4
if z in liste: # z=4 listenin içinde var mı/ if not a in liste diye yazılabilir. not içerisinde yoksa demek.
    print("var")
else: # yoksa bu çalışır
    print("yok")
    

n = "python"
h = "pytho"
h += "n"
if n == h: 
    print("n = h")
else:
    print("n != h")