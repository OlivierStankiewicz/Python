def kodujaca(a):
    gen = ''
    pocz = False
    gen0 = ''
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] == 'A' and a[i + 1] == 'A':
            pocz = True

        elif pocz and a[i] == 'B' and a[i - 1] == 'B':
            pocz = False
            gen0 += 'B'
            gen += gen0
            gen0 = ''

        if pocz == True:
            gen0 += a[i]
    return gen



genotypy=[]
with open('dane_geny.txt') as file:
    for line in file:
        czyst=line.rstrip()
        genotypy.append(czyst)

silnie=0
slabo=0
for genotyp in genotypy:
    anty=genotyp[::-1]
    if genotyp == anty:
        silnie+=1
    elif kodujaca(genotyp) == kodujaca(anty):
        slabo+=1

print(slabo+silnie)
print(silnie)