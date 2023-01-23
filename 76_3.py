def zamiana(n,a,b):
    t=[]
    for z in n:
        t.append(z)
    b-=1
    c=t[a]
    t[a]=t[b]
    t[b]=c
    k=''
    for z in t:
        k+=z
    return k


klucz=[6,2,4,1,5,3]

with open('szyfr3.txt') as file:
    for line in file:
        napis=line.rstrip()


for i in range(len(napis))[::-1]:
    napis=zamiana(napis,i,klucz[i%6])

print(napis)