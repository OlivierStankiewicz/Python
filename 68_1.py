napisy=[]
with open('dane_napisy.txt') as file:
    for line in file:
        t=line.rstrip().split()
        napisy.append(t)

licznik=0
for line in napisy:
    n=line[0][0]
    if len(line[0]) == len(line[1]):
        for i in range(len(line[0])):
            if line[0][i] != n or line[1][i] != n:
                break
        else:
            licznik+=1

print(licznik)