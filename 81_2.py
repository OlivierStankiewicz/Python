def czy(t):
    if t[2]-t[0]==0:
        a=0
    else:
        a=(t[3]-t[1])/(t[2]-t[0])
    b=t[1]-a*t[0]
    if round(a*t[4]+b)==t[5]:
        return True
    print(f'{round(a*t[4]+b)} {t[5]}')
    return False


wsp=[]
with open('wspolrzedne.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        wsp.append(czyst)

for line in wsp:
    for i in range(len(line)):
        line[i]=int(line[i])

licznik=0
for line in wsp:
    if czy(line):
        licznik+=1

print(licznik)