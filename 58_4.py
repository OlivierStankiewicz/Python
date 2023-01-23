import math

czas1=[]
temp=[]
with open('dane_systemy1.txt') as plik1:
    for line in plik1:
        a, b= line.rstrip().split()
        czas1.append(int(a,2))
        temp.append(int(b,2))

skoki=[]
najw=0

for i in range(1095):
    j=i+1
    while j<=1094:
        skok=(temp[i]-temp[j])**2/abs(i-j)
        skoki.append(math.ceil(skok))
        j+=1

for item in skoki:
    if item > najw:
        najw=item

print(najw)