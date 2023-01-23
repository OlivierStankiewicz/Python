import collections
with open('tekst.txt') as file:
    for line in file:
        slowa=line.rstrip().split()

litery={}
licznik=0
for slowo in slowa:
    for litera in slowo:
        if litera not in litery:
            litery[litera]=1
        else:
            litery[litera]+=1
        licznik+=1

odlitery = collections.OrderedDict(sorted(litery.items()))

for item in odlitery:
    print(f'{item} : {odlitery[item]}  ({round(odlitery[item]/licznik*100,2)}%)')