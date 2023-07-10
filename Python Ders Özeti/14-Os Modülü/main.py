import os #OS modülü improt edildi

print(os.getcwd()) # getcwd ile dosya konumumuz terminael yazıldı
print(os.listdir())

os.chdir("4-Tuples ve sets") # klasör içine girmeyi sağlar
print(os.getcwd()) # yeni dosya yolunu verir
print(os.listdir()) # kalsör içindeki dosyaları verir. içerisine girilen dosya yolunun da içerisindeki dosyaları listeler

os.mkdir("yeniKlasör") # bulunan konumda yeniklasör isimli kasör oluşturur.

os.makedirs("klasör1/klasör2/klasör3") # içi içe birden fazla klasör oluşturma

os.rmdir("yeniklasör") # bulunan konumda yeniKlasör isimli klasörü siler.
os.removedirs("klasör1/klasör2/klasör3") # birden fazla klasör silmeye yarar.
os.remove("dosya") #dosya silmeye yarar

os.rename("yeniKlasör", "YeniKlasör") # 1. eski dosya ismi, 2. yeni dosya ismi. dosya ismi değiştirmeye yarar. bir dosyayı farklı bir dizine kopyalamak için de kullanılabilir

print(os.stat("dosya.txt")) # O dosya hakkında bilgileri verir


os.walk() # içerisine girilen dosya yolunun içindeki bütün klasör ve dosyaları dizinler ile birlikte verir
os.path.join() # içerisine girilen dosya yolunu oluşturur

os.path.isfile() # içerisine girilen dosya yolundaki şeyin dosya ise true, klasör ise false çıktısı verir. isdir verirsek lasör ise true, dosya ise false verir.

os.path.splitext() #içerisine girilen dosya yolundaki dosaynın isim ve uzantısını ayrı ayrı verir
