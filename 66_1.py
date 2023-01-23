def suma_cyfr(a):
    s=0
    for cyfra in str(a):
        s+=int(cyfra)
    return s


trojki=[]
with open ('trojki.txt') as file:
    for line in file:
        t=line.rstrip().split()
        for i in range(3):
            t[i] = int(t[i])
        trojki.append(t)

for line in trojki:
    if(suma_cyfr(line[0]) + suma_cyfr(line[1]) == line[2]):
        print(line)