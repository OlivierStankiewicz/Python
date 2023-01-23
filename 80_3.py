def czy_trojk(a,b,c):
    t=[a,b,c]
    t.sort()
    if t[2]<t[0]+t[1]:
        return True
    return False


trojk=[]
with open('dane_trojkaty.txt') as file:
    for line in file:
        czyst=int(line.rstrip())
        trojk.append(czyst)

licznik=0
for i in range(len(trojk)-2):
    for j in range(i+1,len(trojk)-1):
        for k in range(j+1,len(trojk)):
            if czy_trojk(trojk[i],trojk[j],trojk[k]):
                licznik+=1

print(licznik)