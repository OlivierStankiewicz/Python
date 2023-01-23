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

    if czynniki:
        return False
    else:
        return True

ulamki=[]
with open('dane_ulamki.txt') as file:
    for line in file:
        utemp=[]
        a,b=line.rstrip().split()
        utemp.append(int(a))
        utemp.append(int(b))
        ulamki.append(utemp)

licznik=0
for i in ulamki:
    if wsp_czynniki(i[0],i[1]):
        licznik+=1

print(licznik)