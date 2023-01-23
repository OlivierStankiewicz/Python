with open('tekst.txt') as file:
    for line in file:
        slowa=line.rstrip().split()

podslowa=[]
samogloski=['A', 'E', 'I', 'O', 'U', 'Y']

for slowo in slowa:
    najpodsl=''
    najpodsltemp=''
    for i in range(len(slowo)):
        if slowo[i] not in samogloski:
            najpodsltemp+=slowo[i]
        else:
            if len(najpodsltemp)>len(najpodsl):
                najpodsl=najpodsltemp
            najpodsltemp=''

    if len(najpodsltemp) > len(najpodsl):
        najpodsl = najpodsltemp

    podslowa.append(najpodsl)


maxdl=0
licznik=0
for item in podslowa:
    if len(item)>maxdl:
        maxdl=len(item)

for item in podslowa:
    if len(item)==maxdl:
        licznik+=1

print(maxdl)
print(licznik)

for i in range(len(podslowa)):
    if len(podslowa[i])==maxdl:
        print(slowa[i])
        break