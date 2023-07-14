numbers = ["1, 2, 3, 4, 5, 6, 7, 8, 9"]

list1 = [number1 for number1 in numbers] #for döngüsünün kısaltılmış hali. numbers listesini list1'e ekler. matematiksel işlemler başa yazılır
print(list1)

list2 = [number2 for number2 in numbers if number2 * 2 == 10] # koşulumuz en sona gelir

letters = "abcd"
liste3 = [(number3, letter1) for number3 in numbers for letter1 in letters] # iki for döngüsünü iç içe yazma. sıralama önemli!

numbers2 = ["1, 5, 6, 9"]
liste4 = [number4 for number4 in numbers if not number4 in numbers2] #numbers listesinde olup numbers2 listesinde olmayan for döngüsünde çıktı verme
