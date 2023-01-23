genotypy=[]
with open('dane_geny.txt') as file:
    for line in file:
        czyst=line.rstrip()
        genotypy.append(czyst)

geny=[]
maxliczbagen=0
maxdlgenu=0
liczbagen=0
for genotyp in genotypy:
    gen=''
    pocz=False
    gen0=''
    if liczbagen>maxliczbagen:
        maxliczbagen=liczbagen
    liczbagen=0
    for i in range(len(genotyp)):
        if i<len(genotyp)-1 and genotyp[i] == 'A' and genotyp[i+1] == 'A':
            pocz=True

        elif pocz and genotyp[i] == 'B' and genotyp[i-1] == 'B':
            pocz=False
            gen0+='B'
            gen+=gen0
            if len(gen0)>maxdlgenu:
                maxdlgenu=len(gen0)
            gen0=''
            liczbagen+=1

        if pocz==True:
            gen0+=genotyp[i]
    geny.append(gen)

print(maxliczbagen)
print(maxdlgenu)