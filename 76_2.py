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
with open('szyfr2.txt') as file:
    for line in file:
        napisy.append(line.rstrip())
klucz=napisy[1].split()
napisy.remove(napisy[1])

for napis in napisy:
    j=0
    for i in range(len(napis)):
        napis=zamiana(napis,i,klucz[j])
        if j>=len(klucz)-1:
            j=0
        else:
            j+=1
    print(napis)