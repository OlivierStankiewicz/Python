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

rmax=0
licznik = 0
for item in range(100):
    r = ciagi[item][1] - ciagi[item][0]
    if r > 0 and dlugosci[item]>=5:
        for i in range(0,dlugosci[item]-1):
            if ciagi[item][i]+r != ciagi[item][i+1]:
                break
        else:
            licznik+=1
            if r > rmax:
                rmax=r
print(licznik)
print(rmax)