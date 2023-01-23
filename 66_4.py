def czy_trojk(t):
    k=sorted(t)
    if k[0]+k[1]>k[2]:
        return True
    return False


trojki=[]
with open ('trojki.txt') as file:
    for line in file:
        t=line.rstrip().split()
        for i in range(3):
            t[i] = int(t[i])
        trojki.append(t)

licznik=0
ciagmax=0
ciagtemp=0
for item in trojki:
    if czy_trojk(item):
        licznik+=1
        ciagtemp+=1
    else:
        ciagtemp=0
    if ciagtemp>ciagmax:
        ciagmax=ciagtemp

print(licznik)
print(ciagmax)