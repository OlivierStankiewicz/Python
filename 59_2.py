liczby=[]
with open('liczby.txt') as plik:
    for line in plik:
        a=line.rstrip()
        liczby.append(a)

licznik=0
for liczba in liczby:
    a=int(liczba)
    b=int(liczba[::-1])
    if str(a+b)==str(a+b)[::-1]:
        licznik+=1

print(licznik)