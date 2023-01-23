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


fib=[1,1]
for i in range(2,40):
    n=fib[i-2] + fib[i-1]
    fib.append(n)

for item in fib:
    if czy_pierwsza(item):
        print(item)