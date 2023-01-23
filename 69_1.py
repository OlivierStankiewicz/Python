genotypy=[]
with open('dane_geny.txt') as file:
    for line in file:
        czyst=line.rstrip()
        genotypy.append(czyst)

gatunki={}

for genotyp in genotypy:
    if len(genotyp) in gatunki:
        gatunki[len(genotyp)] +=1
    else:
        gatunki[len(genotyp)] =1

maks=0
for i in gatunki:
    if gatunki[i]>maks:
        maks=gatunki[i]

print(len(gatunki))
print(maks)
