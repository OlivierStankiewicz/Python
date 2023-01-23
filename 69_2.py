genotypy=[]
with open('dane_geny.txt') as file:
    for line in file:
        czyst=line.rstrip()
        genotypy.append(czyst)

geny=[]
for genotyp in genotypy:
    gen=''
    pocz=False
    gen0=''
    for i in range(len(genotyp)):
        if i<len(genotyp)-1 and genotyp[i] == 'A' and genotyp[i+1] == 'A':
            pocz=True

        elif pocz and genotyp[i] == 'B' and genotyp[i-1] == 'B':
            pocz=False
            gen0+='B'
            gen+=gen0
            gen0=''

        if pocz==True:
            gen0+=genotyp[i]
    geny.append(gen)

licznik=0
for item in geny:
    if 'BCDDC' in item:
        licznik+=1

print(licznik)
