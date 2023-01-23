napisy=[]
with open('dane_napisy.txt') as file:
    for line in file:
        t=line.rstrip().split()
        napisy.append(t)

licznik=0
for l in napisy:
    if sorted(l[0]) == sorted(l[1]):
        licznik+=1

print(licznik)