def skrot(w):
    S = ['A', 'L', 'G', 'O', 'R', 'Y', 'T', 'M']
    for i in range(8):
        S[i] = ord(S[i])

    for i in range(8-len(w) % 8):
        w += '.'

    n = 0
    for i in range(len(w) // 8):
        for j in range(8):
            S[j] += ord(w[n])
            S[j] %= 128

            n += 1

    wyn = ''
    for i in range(8):
        wyn += chr(65 + S[i] % 26)

    return wyn

def A(y,d,n):
    x=[]
    for i in range(len(y)):
        x.append(y[i]*d%n)

    wyn=''
    for item in x:
        wyn+=chr(item)

    return wyn


wiadomosci=[]
with open('wiadomosci.txt') as file:
    for line in file:
        czyst=line.rstrip()
        wiadomosci.append(czyst)

odczyt=[]
with open('podpisy.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        odczyt.append(czyst)

podpisy=[]
for lista in odczyt:
    podpisytemp=[]
    for item in lista:
        podpisytemp.append(int(item))
    podpisy.append(podpisytemp)


d=3
n=200

for i in range(11):
    if A(podpisy[i],d,n) == skrot(wiadomosci[i]):
        print(i+1)