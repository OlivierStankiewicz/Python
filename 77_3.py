import collections

def czy_litera(a):
    if ord(a) >= ord('A') and ord(a) <=ord('Z'):
        return True
    return False


odczyt=[]
with open('szyfr.txt') as file:
    for line in file:
        czyst=line.rstrip()
        odczyt.append(czyst)
tekst=odczyt[0]

litery={}
for znak in tekst:
    if czy_litera(znak) and znak not in litery:
        litery[znak]=1
    elif czy_litera(znak):
        litery[znak]+=1

literysort=collections.OrderedDict(sorted(litery.items()))

n=0
suma=0
for item in literysort:
    print(f'{item} : {literysort[item]}')
    n+=literysort[item]
    suma+=literysort[item]*(literysort[item]-1)

ko=suma/(n*(n-1))
d=0.0285/(ko-0.0385)
print(f'szacunkowa długość: {round(d,2)}')
print(f'długośc faktyczna: {len(odczyt[1])}')