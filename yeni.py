def asal_mi(sayi):
    if sayi > 1:
        for i in range(2, sayi):
            if sayi % i == 0:
                print('degil') 
                break # Bir tam sayıya bölündüyse asal değildir.
        else:
                print('asal')  # Tüm bölünebilirlik kontrollerinden geçtiyse asal sayıdır.
    else:
        print('degildir')

asal_mi(6)
# 14. Bir Sayının Asal Olup Olmadığını Kontrol Etme
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, bir sayının asal olup olmadığını kontrol etsin 
# ve sonuç olarak True (asal) veya False (asal değil) döndürsün. 
# Örneğin, asal_mi(29) çağrıldığında True, asal_mi(10) çağrıldığında False döndürmelidir.
# def asal_mi(sayi):
#     if sayi < 2:
#         return False
#     for i in range(2, sayi):
#         if sayi % i == 0:
#             return False
#     return True
# print(asal_mi(2))