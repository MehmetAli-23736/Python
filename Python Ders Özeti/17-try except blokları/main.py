try: # içerisinde olası hata olabilecek kod bölümü buraya yazılır
    a = 5
    b = 10
    c = a / b
    d = x #burda bir hatamız var
  
except ZeroDivisionError: # özel hata, payda sıfır olamaz
    print("payda sıfır olamaz") #try içinde hatamız var ise bu çıktı verir
    
      
except: # içerisine girilen koda göre hatanın farklılığı ile burası çalışır
    print("hata oluştu") #try içinde hatamız var ise bu çıktı verir
    
else:
    print("else bloğu çalıştı")

finally:
    print("finally bloğu çalıştı")

if d == x: # özel hata oluşturulabilir
    raise ZeroDivisionError