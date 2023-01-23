czas1=[]
temp1=[]
with open('dane_systemy1.txt') as plik1:
    for line in plik1:
        a, b= line.rstrip().split()
        czas1.append(int(a,2))
        temp1.append(int(b,2))

czas2=[]
temp2=[]
with open('dane_systemy2.txt') as plik2:
    for line in plik2:
        a, b= line.rstrip().split()
        czas2.append(int(a,4))
        temp2.append(int(b,4))

czas3=[]
temp3=[]
with open('dane_systemy3.txt') as plik3:
    for line in plik3:
        a, b= line.rstrip().split()
        czas3.append(int(a,8))
        temp3.append(int(b,8))

popr1=czas1[0]
popr2=czas2[0]
popr3=czas3[0]
licznik=0

for item in range(1095):
    if czas1[item] != popr1 and czas2[item] != popr2 and czas3[item] != popr3:
        licznik+=1
    popr1 += 24
    popr2 += 24
    popr3 += 24

print(licznik)