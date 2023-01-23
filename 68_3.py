napisy=[]
with open('dane_napisy.txt') as file:
    for line in file:
        t=line.rstrip().split()
        napisy.append(t)

anagr={}

for i in napisy:
    for j in i:
        j=sorted(j)
        k=''
        for c in j:
            k+=c
        if k not in anagr:
            anagr[k] = 1
        else:
            anagr[k] +=1

maks=0
for i in anagr:
    if anagr[i] > maks:
        maks=anagr[i]

print(maks)