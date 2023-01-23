def czy_trojk(a,b,c):
    if a<b+c:
        return True
    return False


trojk=[]
with open('dane_trojkaty.txt') as file:
    for line in file:
        czyst=int(line.rstrip())
        trojk.append(czyst)

trojk.sort(reverse=True)

for i in range(len(trojk)-2):
    if czy_trojk(trojk[i],trojk[i+1],trojk[i+2]):
        print(trojk[i]+trojk[i+1]+trojk[i+2])
        break