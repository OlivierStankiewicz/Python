ciagi=[]
with open('ciagi.txt') as file:
    for line in file:
        czyst=line.rstrip()
        ciagi.append(czyst)

licznik=0

for item in ciagi:
    p=int(item[0])
    for j in range(1,len(item)):
        if p+int(item[j]) == 2:
            break
        else:
            p=int(item[j])
    else:
        licznik+=1

print(licznik)