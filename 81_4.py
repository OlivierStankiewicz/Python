def czypr(t):
    ab=(t[0]-t[2])**2+(t[1]-t[3])**2
    ac=(t[0]-t[4])**2+(t[1]-t[5])**2
    bc=(t[2]-t[4])**2+(t[3]-t[5])**2
    t=[ab,ac,bc]
    t.sort()
    if t[0]+t[1]==t[2]:
        return True
    return False

wsp=[]
with open('wspolrzedneTR.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        wsp.append(czyst)

for line in wsp:
    for i in range(len(line)):
        line[i]=int(line[i])

licznik=0
for line in wsp:
    if czypr(line):
        licznik+=1

print(licznik)