import time 
def zaman_hesapla(fonk):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        fonk(*args, **kwargs)
        bitis = time.time()
        print(f" işlem {bitis - baslangic} saniye sürdü.")
     
    return wrapper

@zaman_hesapla
def kareleri_al(liste):
    for i in liste:
        print(i * i)
        
@zaman_hesapla
def küpleri_al(liste):
    for i in liste:
        print(i ** 3)
    
@zaman_hesapla
def topla(a, b):
    time.sleep(1)
    print(a + b)
    
kareleri_al(range(100))
küpleri_al(range(100))
topla(10, 20)

