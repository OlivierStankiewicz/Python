def szyfrowanie(n,a,b):
    wyn=ord(n)-ord('a')
    wyn*=a
    wyn+=b
    if wyn>25:
        wyn=wyn%26
    wyn+=ord('a')
    return chr(wyn)


with open('tekst.txt') as file:
    for line in file:
        slowa=line.rstrip().split()

a=5
b=2

for slowo in slowa:
    if len(slowo)>=10:
        nowesl=''
        for litera in slowo:
            nowesl+=szyfrowanie(litera,a,b)
        print(nowesl)