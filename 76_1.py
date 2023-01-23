def zamiana(n,a,b):
    t=[]
    for z in n:
        t.append(z)
    a=int(a)
    b=int(b)-1
    c=t[a]
    t[a]=t[b]
    t[b]=c
    k=''
    for z in t:
        k+=z
    return k


napisy=[]
klucz=[]
with open('szyfr1.txt') as file:
    for line in file:
        napisy.append(line.rstrip())
klucz=napisy[6].split()
napisy.remove(napisy[6])

for napis in napisy:
    for i in range(len(napis)):
        napis=zamiana(napis,i,klucz[i])
    print(napis)