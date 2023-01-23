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

mintemp=[]
mintemp.append(temp1[0])
mintemp.append(temp2[0])
mintemp.append(temp3[0])

for temp in temp1:
    if temp<mintemp[0]:
        mintemp[0]=temp

for temp in temp2:
    if temp<mintemp[1]:
        mintemp[1]=temp

for temp in temp3:
    if temp<mintemp[2]:
        mintemp[2]=temp

for item in range(len(mintemp)):
    if str(mintemp[item])[0]=='-':
        mintemp[item]='-'+bin(mintemp[item])[3:]
    else:
        item=bin(mintemp[item])[3:]

print(mintemp[0])
print(mintemp[1])
print(mintemp[2])