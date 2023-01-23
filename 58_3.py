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

licznik=1
rekord1=temp1[0]
rekord2=temp2[0]
rekord3=temp3[0]
for item in range(1095):
    czy1 = False
    czy2 = False
    czy3 = False
    if temp1[item]>rekord1:
        czy1 = True
        rekord1 = temp1[item]

    if temp2[item]>rekord2:
        czy2 = True
        rekord2 = temp2[item]

    if temp3[item]>rekord3:
        czy3 = True
        rekord3 = temp3[item]

    if czy1 or czy2 or czy3:
        licznik+=1

print(licznik)