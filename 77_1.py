import math
def szyfrowanie(a,b):
    i=ord(a)-ord('A')
    j=ord(b)-ord('A')
    wyn=(i+j)%26+ord('A')
    return chr(wyn)


with open('dokad.txt') as file:
    for line in file:
        tekst=line.rstrip()

zaszyfrowany=''
klucz='LUBIMYCZYTAC'
idklucz=0
liczliter=0
for znak in tekst:
    if ord(znak) >= ord('A') and ord(znak) <= ord('Z'):
        zaszyfrowany+=szyfrowanie(znak,klucz[idklucz%len(klucz)])
        idklucz+=1
        liczliter+=1
    else:
        zaszyfrowany+=znak

print(math.ceil(liczliter/len(klucz)))
print(zaszyfrowany)