def szyfrowanie(a,b):
    i=ord(a)-ord('A')
    j=ord(b)-ord('A')
    wyn=(i-j)%26+ord('A')
    return chr(wyn)


t=[]
with open('szyfr.txt') as file:
    for line in file:
        czyst=line.rstrip()
        t.append(czyst)

tekst=t[0]
klucz=t[1]
odszyfrowany=''
idklucz=0

for znak in tekst:
    if ord(znak) >= ord('A') and ord(znak) <= ord('Z'):
        odszyfrowany += szyfrowanie(znak, klucz[idklucz % len(klucz)])
        idklucz += 1
    else:
        odszyfrowany += znak

print(odszyfrowany)