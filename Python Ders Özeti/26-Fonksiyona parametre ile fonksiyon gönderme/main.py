liste1 = [1,2,3,4,5]
liste2 = [3,4,5,7,9,10,12]

def kare_al(x):
    return x * x
def kup_al(x):
    return x ** 3

def map_fonk(fonk, liste):
    sonuc = []
    for i in liste:
        sonuc.append(fonk(i))
    return sonuc

print(map_fonk(kare_al, liste1))

print(map_fonk(kup_al, liste2))
