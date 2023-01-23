hasla=[]
with open('hasla.txt') as file:
    for line in file:
        czyst=line.rstrip()
        hasla.append(czyst)

lista=[]
powtorz=[]

for item in hasla:
    if item not in lista:
        lista.append(item)
    elif item in lista and item not in powtorz:
        powtorz.append(item)

powtorz.sort()

print(powtorz)