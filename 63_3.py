import math

def czy_pierwsza(a):
    if a<2:
        return False
    n=2
    while n<=math.sqrt(a):
        if a%n==0:
            return False
        n+=1
    else:
        return True


ciagi=[]
with open('ciagi.txt') as file:
    for line in file:
        czyst=line.rstrip()
        ciagi.append(int(czyst,2))

licznik=0
maks=ciagi[0]
mini=ciagi[0]

for item in ciagi:
    if item >1:
        n=2
        a=0
        while n<=math.sqrt(item):
            if czy_pierwsza(n) and item%n==0 and czy_pierwsza(item/n):
                licznik+=1
                if item>maks:
                    maks=item
                elif item<mini:
                    mini=item
            n+=1

print(licznik)
print(f'''najwieksza: {maks}
najmniejsza: {mini}''')