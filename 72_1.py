napisy=[]
with open('napisy.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        napisy.append(czyst)

licznik=0
napisy2=[]
for line in napisy:
    if len(line[0]) >= 3*len(line[1]) or len(line[1]) >= 3*len(line[0]):
        licznik+=1
        napisy2.append(line)

print(licznik)
print(napisy2[0])