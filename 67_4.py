fib=[1,1]
for i in range(2,40):
    n=fib[i-2] + fib[i-1]
    fib.append(n)

fraktal=[]
for item in fib:
    fraktal.append(str(bin(item)[2:]))

for item in fraktal:
    licznik=0
    for znak in item:
        if znak=='1':
            licznik+=1
    if licznik==6:
        print(item)