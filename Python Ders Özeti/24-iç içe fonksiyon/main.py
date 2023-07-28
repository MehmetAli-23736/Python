def hesaplamalar(x):
    def kare_al(a):
        return a ** 2
    
    def karekok_al(a):
        return a ** 0.5
    
    def faktoriyel(a):
        carpim  = 1
        for i in range(1, a + 1):
            carpim *= i
        return carpim
    kare = kare_al(x)
    karekok = karekok_al(x)
    fakt = faktoriyel(x)
    return f"karesi: {kare}, karekökü: {karekok}, faktöriyel: {fakt}"

def toplam_carpim(*args):
    def toplama(demet):
        return sum(demet)
    def carpma(demet):
        carpim = 1
        for i in demet:
            carpim *= i
        return carpim
    
    return f"toplamları: {toplama(args)}, çarpımları: {carpma(args)}"


print(toplam_carpim(2,3,4,5,6))

print(hesaplamalar(9))