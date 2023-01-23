def szyfrowanie(n,a,b):
    wyn=''
    for litera in n:
        x=ord(litera)-ord('a')
        x*=a
        x+=b
        if x>25:
            x%=26
        x+=ord('a')
        wyn+=chr(x)
    return wyn


slowa=[]
with open('probka.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        slowa.append(czyst)

szyfrujace=[]
deszyfrujace=[]
for line in slowa:
    for a in range(26):
        for b in range(26):
            if szyfrowanie(line[0],a,b)==line[1]:
                lol=[a,b]
                szyfrujace.append(lol)
            if szyfrowanie(line[1],a,b)==line[0]:
                cs=[a,b]
                deszyfrujace.append(cs)

for i in range(5):
    print(szyfrujace[i])
    print(deszyfrujace[i])