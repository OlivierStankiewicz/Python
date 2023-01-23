def A(y,d,n):
    x=[]
    for i in range(len(y)):
        x.append(y[i]*d%n)

    wyn=''
    for item in x:
        wyn+=chr(item)

    return wyn


odczyt=[]
with open('podpisy.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        odczyt.append(czyst)

podpisy=[]
for lista in odczyt:
    podpisytemp=[]
    for item in lista:
        podpisytemp.append(int(item))
    podpisy.append(podpisytemp)

d=3
n=200

odszyfr=[]
for item in podpisy:
    odszyfr.append(A(item,d,n))

for i in odszyfr:
    print(i)