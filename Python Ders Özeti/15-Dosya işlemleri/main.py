f = open("\\Users\\Mehmet Ali TAŞ\\Desktop\\Python Özeti\\15-Dosya işlemleri\\belge.txt", "r") # open diyerek açacağımız dosya dizinini ve "r" diyerek read modunu aktif ediyoruz
icerik = f.read() #içeriği okuyoruz. içerisine girilen değere göre o kadar karakter okur
print(icerik) # içeriği yazdırıyoruz
f.close() # dosyayı kapatıyoruz. 

with open("dosya yolu", "işlem") as f: # dosyayı kapatması otomatik olarak gerçekleşmesi için bunu kullanabiliriz.
    icerik2 = f.read()
    print(icerik2)
    
icerik3 = f.readlines() # her satırı bir eleman olarak alır ve bunu listeye çevirir
icerik3 = f.readline() # sadece 1 satır okur.

pozsyon = f.tell() # imlecin kaçcıncı karakterde olduğunu verir
print(pozsyon) # pozisyonu yazdırır

f.seek(0) #imleci verilen değere göre konumlandırma

f2 = open("dosya", "w") # dosya içerisine veri yazdırmayı sağlar. dosyayı sıfırdan oluşturur. içerik silinip yenisi yazılır
yazdir = f2.write("Merhaba") # yazılacak veri buraya verilir

f2 = open("dosya", "a") # dosyanın sonuna write etmek için kullanılır

f3 = open("dosya", "rb") # b metin harici veri okumak için kullanılır.