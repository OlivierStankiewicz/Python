ulamki=[]
with open('dane_ulamki.txt') as file:
    for line in file:
        utemp=[]
        a,b=line.rstrip().split()
        utemp.append(int(a))
        utemp.append(int(b))
        ulamki.append(utemp)

suma=0
b=2*2*3*3*5*5*7*7*13
for item in ulamki:
    a=b/item[1]
    suma+=item[0]*a

print(suma)