import math

def czy_pierwsza(a):
    if a<2:
        return False
    n=2
    while n<=math.sqrt(a):
        if a%n==0:
            return False
        n+=1
    return True


trojki=[]
with open ('trojki.txt') as file:
    for line in file:
        t=line.rstrip().split()
        for i in range(3):
            t[i] = int(t[i])
        trojki.append(t)

for l in trojki:
    if(czy_pierwsza(l[0]) and czy_pierwsza(l[1]) and l[0]*l[1]==l[2]):
        print(l)