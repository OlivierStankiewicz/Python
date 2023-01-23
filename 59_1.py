import math

def czy_pierwsza(a):
    if a<2:
        return False
    i=2
    while i<=math.sqrt(a):
        if a%i==0:
            return False
        i+=1
    return True


liczby=[]
with open('liczby.txt') as plik:
    for linia in plik:
        a=linia.rstrip()
        liczby.append(int(a))
#liczby=[32,210,1331,1157625,105,429,1287,3465,255255]
#NIE WIADOMO DLACZEGO WYCHODZI ZADANIE ŹLE LOL

licznik=0

for liczba in liczby:
    if liczba%2==1:
        dobre_czynniki = []
        i=3
        while i<=math.sqrt(liczba):
            if liczba%i==0:
                if czy_pierwsza(i) and i not in dobre_czynniki:
                    dobre_czynniki.append(i)
            i+=2
        if len(dobre_czynniki) == 3:
            licznik+=1
            print(dobre_czynniki)
print(licznik)