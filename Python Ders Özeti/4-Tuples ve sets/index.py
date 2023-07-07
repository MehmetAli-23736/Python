demet = ("sarı", "siyah", "yeşil", "kırmızı", "mavi") # tuple(demet) oluştruduk
# listeler ile aynı fonksiyonlar kullanılabilir. Fakat demete eleman ekleyemez-silemez-değiştiremezsiniz.


kume = {"sarı", "siyah", "yeşil", "kırmızı", "mavi"} #küme oluşturduk
# listeler ile aynı fonksiyonlar kullanılabilir. Kümeler sırasız veri yapısına sahiptir.
kume.add("pembe") # kümeye eleman ekleme
kume.remove("siyah") # kümeden eleman siler. Kümede olamayan eleman silinmeye çalışırsa hata verir
kume.discard("gri") # kümede olmayan elemanı silme işlemi yaparsak hata almadan çıktı verir

kume1 = { "sarı", "siyah", "yeşil", "kırmızı", "mavi"}
kume2 = {"sarı", "siyah", "yeşil", "beyaz", "gri"}

print(kume2.intersection(kume1)) # kume1 ve kume2deki ortak elemanları verir
print(kume1.union(kume2)) #2 kümeyi birleştirir. Aynı elemanları 1 kez yazar
print(kume1.difference(kume2)) # kume1 de olup kume2 de olamayn elemanları yadırır
print("sarı" in kume1) # sarı, kume1 içerisinde var mı -> true


boslist1 = []
boslist2 = list()

bosdemet1 = ()
bosdemet2 = tuple()

boskume2 = {}
boskume1 = set() #bu bir sözlüktür.

python = set("PYTHON") # bunu küme olarak görür ve harfleri birer eleman olarak alır
print(python)

