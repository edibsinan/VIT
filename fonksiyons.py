def kareAl(sayi):
    return sayi**2


def topla(a,b):
    return a+b

def sayHello():
    print ("Hello World")

def cokluYazdir(metin,kere):
    print( metin*kere)

def listeYap(*params):
    liste=[]
    for i in params:
        liste.append(i)
    return liste

def asalBul(sayi):
    if sayi<2:
        print('degildir')
        for i in range(2,sayi):
            if sayi%i==0:
                print('degildir')
    print('asaldir')



