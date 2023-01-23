def moc_liczby(a):
    k=0
    while a>9:
        b=1
        for cyfra in str(a):
            b*=int(cyfra)
        a=b
        k+=1
    return(k)


liczby=[]
with open('liczby.txt') as plik:
    for line in plik:
        a=line.rstrip()
        liczby.append(int(a))

jedynkowe=[]
moce=[0,0,0,0,0,0,0,0]

for n in liczby:
    if moc_liczby(n)<9:
        moce[moc_liczby(n)-1]+=1
    if moc_liczby(n)==1:
        jedynkowe.append(n)

najw=jedynkowe[0]
najmn=jedynkowe[0]
for item in jedynkowe:
    if item > najw:
        najw=item
    elif item <najmn:
        najmn=item

print(moce)
print(najmn)
print(najw)