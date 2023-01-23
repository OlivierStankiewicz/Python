def wsp_czynniki(a,b):
    n=2
    czynniki=[]
    czynniki_a=[]
    while a>1:
        while a%n==0:
            czynniki_a.append(n)
            a/=n
        n+=1

    n=2
    while b>1:
        while b%n==0:
            if n in czynniki_a:
                czynniki.append(n)
                czynniki_a.remove(n)
            b/=n
        n+=1

    return czynniki

ulamki=[]
with open('dane_ulamki.txt') as file:
    for line in file:
        utemp=[]
        a,b=line.rstrip().split()
        utemp.append(int(a))
        utemp.append(int(b))
        ulamki.append(utemp)

for item in ulamki:
    for j in wsp_czynniki(item[0],item[1]):
        item[0]/=j
        item[1] /= j

suma=0
for item in ulamki:
    suma+=item[0]

print(suma)