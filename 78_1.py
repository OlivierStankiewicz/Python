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


wiadomosci=[]
with open('wiadomosci.txt') as file:
    for line in file:
        czyst=line.rstrip()
        wiadomosci.append(czyst)

wiad=wiadomosci[0]

for i in range(8-len(wiad)%8):
    wiad+='.'

print(f'a: {len(wiad)}')

S = ['A', 'L', 'G', 'O', 'R', 'Y', 'T', 'M']
for i in range(8):
    S[i] = ord(S[i])

n=0
for i in range(len(wiad)//8):
    for j in range(8):
        S[j]+=ord(wiad[n])
        S[j]%=128
        n+=1

print(f'b: {S}')

wyn=''

for i in range(8):
    wyn+=chr(65+ S[i]%26)

print(f'c: {skrot(wiad)}')