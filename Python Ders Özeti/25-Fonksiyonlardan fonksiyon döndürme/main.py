def islem_sec(islem):
    def toplama(*args):
        toplam = 0
        for arg in args:
            toplam += arg
        return toplam
    
    def carpma(*args):
        carpim = 1
        for arg in args:
            carpim *= arg
        return carpim
    
    def ortalama(*args):
        return sum(args) / len(args)
    
    if islem == "toplama":
        return toplama
    elif islem == "carpma":
        return carpma
    elif islem == "ortalama":
        return ortalama
    
top_fonk = islem_sec("toplama")
carpma_fonk = islem_sec("carpma")
ortalama_fonk = islem_sec("ortalama")
print(top_fonk(1, 2, 3))
print(carpma_fonk(2, 3, 4))
print(ortalama_fonk(3, 4, 5))


##########################################################


def kisi_sec(kisi):
    def takim_sec(takim):
        return f"{kisi}, {takim} takımını tutuyor"
    return takim_sec

a = kisi_sec("ahmet")
b = kisi_sec("ali")

print(a("Trabzonspor"))
print(b("Beşiktaş"))