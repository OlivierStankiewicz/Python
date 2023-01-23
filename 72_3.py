napisy=[]
with open('napisy.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        napisy.append(czyst)

dlugosci={}

for line in napisy:
    licznik=0
    n=-1
    while 1:
        if line[0][n]==line[1][n]:
            licznik+=1
        else:
            break
        n-=1
    if licznik not in dlugosci:
        dlugosci[licznik]=1
    else:
        dlugosci[licznik]+=1

print(max(dlugosci))

for line in napisy:
    licznik=0
    n=-1
    while 1:
        if line[0][n]==line[1][n]:
            licznik+=1
        else:
            break
        n-=1
    if licznik==max(dlugosci):
        print(line)