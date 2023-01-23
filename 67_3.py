fib=[1,1]
for i in range(2,40):
    n=fib[i-2] + fib[i-1]
    fib.append(n)

fraktal=[]
for item in fib:
    fraktal.append(str(bin(item)[2:]))

for i in range(len(fraktal)):
    if len(fraktal[i])<len(fraktal[39]):
        fraktal[i] = (len(fraktal[39]) - len(fraktal[i])) * '0' + fraktal[i]

for item in fraktal:
    print(item)
