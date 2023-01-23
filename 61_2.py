odczyt = []
with open('ciagi.txt') as file:
    for line in file:
        a = line.rstrip()
        odczyt.append(a)

ciagi = []
dlugosci = []
n = 0
while n<200:
    ciagitemp = []
    ciagitemp2 = []
    if n%2 == 0:
        dlugosci.append(int(odczyt[n]))
    else:
        ciagitemp = odczyt[n].split()
        for item in ciagitemp:
            ciagitemp2.append(int(item))
        ciagi.append(ciagitemp2)
    n+=1

szesciany = []
b=1
c=2
while b<=1000000:
    szesciany.append(b)
    b=c**3
    c+=1

maksymalne = []

for ciag in ciagi:
    maks = 0
    for liczba in ciag:
        if liczba in szesciany and liczba>maks:
            maks = liczba
    if maks != 0:
        maksymalne.append(maks)

print(maksymalne)